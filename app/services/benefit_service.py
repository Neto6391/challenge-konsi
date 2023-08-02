
import asyncio
from typing import List


from app.producer.producer import Producer
from app.consumer.consumer import Consumer
from app.utils.rabbitmq_manager_factory import RabbitMQFactory
from config.logging import logger

class BenefitService:
    def __init__(self):
        self.rabbitmq_manager = None
        self.producer_cpf = None
        self.consumer_cpf = None

    async def initialize(self):
        self.rabbitmq_manager = await RabbitMQFactory.create_rabbitmq_manager()
        self.producer_cpf = Producer(self.rabbitmq_manager, queue_name="cpf_queue")
        self.consumer_cpf = Consumer(self.rabbitmq_manager, queue_name="cpf_queue")

    async def add_queue_cpf_benefit_async(self, cpf: str):
        try:
            await self.producer_cpf.publish_message(cpf)
        except Exception as e:
            logger.error(f"Error adding CPF to queue: {e}")
            raise
        
    async def add_queue_cpf_benefit_list_async(self, cpfList: List[str]):
        try:

            tasks = [self.add_queue_cpf_benefit_async(cpf) for cpf in cpfList]
            await asyncio.gather(*tasks)
        except Exception as e:
            logger.error(f"Error adding CPFs to queue: {e}")
            raise
    
    async def process_cpf_benefit_queue_async(self, input_callback):
        await self.consumer_cpf.start_consuming(input_callback=input_callback)

        