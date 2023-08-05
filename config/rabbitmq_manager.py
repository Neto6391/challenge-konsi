import aio_pika
from config.logging import logger

class RabbitMQManager:
    def __init__(self, host, port, user, password, virtual_host):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.virtual_host = virtual_host
        self.connection = None
        self.channel = None

    async def create_connection(self):
        try:
            self.connection = await aio_pika.connect_robust(
                host=self.host,
                port=self.port,
                virtualhost=self.virtual_host,
                login=self.user,
                password=self.password
            )
            self.channel = await self.connection.channel()
            logger.info("RabbitMQ Connected!")
        except aio_pika.exceptions.AMQPError as e:
            logger.error(f"Error connecting to RabbitMQ: {e}")
            raise

    async def close_connection(self):
        try:
            await self.connection.close()
            logger.info("Desconnect RabbitMQ")
        except aio_pika.exceptions.AMQPError as e:
            logger.error(f"Error closing connection: {e}")
            raise

    async def create_queue(self, queue_name):
        try:
            await self.channel.declare_queue(queue_name)
            logger.info("Created a queue")
        except aio_pika.exceptions.AMQPError as e:
            logger.error(f"Error creating queue: {e}")
            raise

    async def publish_message(self, queue_name, message):
        try:
            message = aio_pika.Message(
                body=message.encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT
            )
            await self.channel.default_exchange.publish(
                message,
                routing_key=queue_name
            )
            logger.info("Queue is published!")
        except aio_pika.exceptions.AMQPError as e:
            logger.error(f"Error publishing message to queue '{queue_name}': {e}")
            raise

    async def consume(self, queue_name, callback):
        try:
            queue = await self.channel.declare_queue(queue_name)
            await queue.consume(callback)
            logger.info("Consuming queue: {queue_name}")
        except aio_pika.exceptions.AMQPError as e:
            logger.error(f"Error consuming queue: {e}")
            raise
