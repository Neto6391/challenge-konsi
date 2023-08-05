
import asyncio
from typing import List



from api.producer.producer import Producer
from api.consumer.consumer import Consumer
from api.utils.consumer_singleton import ConsumerSingleton
from api.utils.producer_singleton import ProducerSingleton
from config.logging import logger
from config.rabbitmq_manager import RabbitMQManager

class BenefitService:
    def __init__(self, rabbitmq_manager: RabbitMQManager, queue_name: str):
        self.rabbitmq_manager = rabbitmq_manager
        self.queue_name = queue_name
        self.producer_cpf = None
        self.consumer_cpf = None
        

    async def initialize(self):
        self.producer_cpf = ProducerSingleton.get_instance(rabbitmq_manager=self.rabbitmq_manager, queue_name=self.queue_name)
        self.consumer_cpf = ConsumerSingleton.get_instance(self.rabbitmq_manager, queue_name=self.queue_name)

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
            cpfList = []
        except Exception as e:
            logger.error(f"Error adding CPFs to queue: {e}")
            raise
    
    async def process_cpf_benefit_queue_async(self, input_callback):
        await self.consumer_cpf.start_consuming(input_callback=input_callback)

        