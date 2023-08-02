from config.rabbitmq_config import RabbitMQManager
from config.logging import logger

class Producer:
    def __init__(self, rabbitmq_manager: RabbitMQManager, queue_name: str):
        self.rabbitmq_manager = rabbitmq_manager
        self.queue_name = queue_name


    async def publish_message(self, message):
        try:
            await self.rabbitmq_manager.publish_message(self.queue_name, message)
        except Exception as e:
            logger.error(f"Error posting message to queue {self.queue_name}: {e}")
            raise