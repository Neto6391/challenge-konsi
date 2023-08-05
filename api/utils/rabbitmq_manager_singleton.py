from api.utils.rabbitmq_manager_factory import RabbitMQFactory
from config.rabbitmq_manager import RabbitMQManager

class RabbitMQManagerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            rabbitmq_factory = RabbitMQFactory()
            cls._instance.rabbitmq_manager = rabbitmq_factory.create_rabbitmq_manager()
        return cls._instance

    def get_rabbitmq_manager(self) -> RabbitMQManager:
        return self.rabbitmq_manager