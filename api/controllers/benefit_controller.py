import asyncio
from api.schemas.cpf_benefit_data import CPFBenefitData
from api.services.benefit_service import BenefitService
from config.logging import logger
from web_crawler_app.main import crawl_benefit_cpf

class BenefitController:
    def __init__(self):
        self.consumer_data: CPFBenefitData = None
        self.benefit_service = BenefitService()

    async def crawl_portal_extrato_consumer(self, cpf):
        logger.info(f"Consuming Queue")
        await crawl_benefit_cpf(username=self.consumer_data.username, password=self.consumer_data.password, cpf=cpf)
        

    async def create_benefit_by_cpf(self, data: CPFBenefitData):
        try:
            self.consumer_data = data
            await self.benefit_service.initialize()
            await self.benefit_service.add_queue_cpf_benefit_list_async(data.cpf)
            await self.benefit_service.process_cpf_benefit_queue_async(input_callback=self.crawl_portal_extrato_consumer)
        except Exception as e:
            logger.error(f'Found error in processing queues: {e}')
            raise