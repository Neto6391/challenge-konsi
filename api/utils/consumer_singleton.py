from api.consumer.consumer import Consumer
from config.rabbitmq_manager import RabbitMQManager


class ConsumerSingleton:
    _instance = None

    @classmethod
    def get_instance(cls, rabbitmq_manager: RabbitMQManager, queue_name: str):
        if cls._instance is None:
            cls._instance = Consumer(rabbitmq_manager, queue_name=queue_name)
        return cls._instance