import aio_pika
from config.rabbitmq_config import RabbitMQManager
from config.logging import logger

class Consumer:
    def __init__(self, rabbitmq_manager: RabbitMQManager, queue_name: str):
        self.rabbitmq_manager = rabbitmq_manager
        self.queue_name = queue_name
    

    async def start_consuming(self, input_callback):
        await self.rabbitmq_manager.consume(queue_name=self.queue_name, callback=lambda msg: self.handle_message(msg, input_callback))

    async def handle_message(self, message: aio_pika.IncomingMessage, input_callback):
        async with message.process():
            body = message.body.decode()
            logger.info(f"Received: {body}")

            try:
                if input_callback is not None:
                    await input_callback(body)
            
            except Exception as e:
                logger.error(f"Error processing message: {e}")

            