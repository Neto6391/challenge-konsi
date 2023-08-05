import asyncio
from api.repository.benefit_repository import BenefitRepository
from api.schemas.cpf_benefit_data import CPFBenefitData
from api.services.benefit_service import BenefitService
from config.logging import logger
from config.rabbitmq_manager import RabbitMQManager
from config.redis_config import RedisCache
from web_crawler_app.main import crawl_benefit_cpf


class BenefitController:
    def __init__(self, rabbitmq_manager: RabbitMQManager, redis_cache: RedisCache, benefit_repository: BenefitRepository):
        self.consumer_data: CPFBenefitData = None
        self.benefit_service = BenefitService(rabbitmq_manager=rabbitmq_manager, queue_name="cpf_queue")
        self.redis_cache = redis_cache
        self.benefit_repository = benefit_repository

    async def crawl_portal_extrato_consumer(self, cpf):
        try:
            logger.info(f"Consuming Queue")
            has_cpf = self.redis_cache.get_data(cpf)
            if has_cpf is None:
                benefit = await crawl_benefit_cpf(username=self.consumer_data.username, password=self.consumer_data.password, cpf=cpf)
                if benefit is not None:
                    self.redis_cache.store_data(cpf, benefit)
                    await self.benefit_repository.index_document(index_name="cpf_index", id=cpf, data={
                        "cpf": cpf,
                        "benefit": int(benefit)
                    })
            else:
                benefit = has_cpf
                await self.benefit_repository.index_document(index_name="cpf_index", id=cpf, data={
                        "cpf": cpf,
                        "benefit": int(benefit)
                    })
            logger.info(f"Consumer Queue -> {benefit}")
            
        except Exception as e:
            logger.error(f'Error when consuming queue {e}')

    async def create_benefit_by_cpf(self, data: CPFBenefitData):
        try:
            self.consumer_data = data

            await asyncio.gather(self.benefit_service.initialize())
            loop = asyncio.get_running_loop()
            loop.create_task(self.benefit_service.add_queue_cpf_benefit_list_async(data.cpf))
            await self.benefit_service.process_cpf_benefit_queue_async(input_callback=self.crawl_portal_extrato_consumer)
            
        except Exception as e:
            logger.error(f'Found error in processing queues: {e}')
            raise
    