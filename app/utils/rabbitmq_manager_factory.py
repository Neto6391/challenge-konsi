import os
from config.environment import get_config
from config.rabbitmq_config import RabbitMQManager


class RabbitMQFactory:
    @staticmethod
    async def create_rabbitmq_manager() -> RabbitMQManager:
        config = get_config(os.environ.get('ENVIRONMENT'))
        rabbitmq_host = config.RABBITMQ_HOST
        rabbitmq_port = config.RABBITMQ_PORT
        rabbitmq_user = config.RABBITMQ_USER
        rabbitmq_pass = config.RABBITMQ_PASS
        rabbitmq_vhost = config.RABBITMQ_VHOST

        rabbitmq_manager =  RabbitMQManager(rabbitmq_host, rabbitmq_port, rabbitmq_user, rabbitmq_pass, rabbitmq_vhost)
        await rabbitmq_manager.create_connection()
        return rabbitmq_manager