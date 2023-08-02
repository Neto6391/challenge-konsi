from app.schemas.cpf_benefit_data import CPFBenefitData
from app.services.benefit_service import BenefitService
from config.logging import logger

class BenefitController:
    benefit_service = BenefitService()

    def get_hello_callback_consumer(self, message):
        logger.info(f"Hello -> input: {message}")

    async def create_benefit_by_cpf(self, data: CPFBenefitData):
        try:
            await self.benefit_service.initialize()
            await self.benefit_service.add_queue_cpf_benefit_list_async(data.cpf)
            await self.benefit_service.process_cpf_benefit_queue_async(input_callback=self.get_hello_callback_consumer)
        except Exception as e:
            logger.error(f'Found error in processing queues: {e}')
            raise