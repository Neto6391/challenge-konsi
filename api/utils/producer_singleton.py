from api.producer.producer import Producer
from config.rabbitmq_manager import RabbitMQManager


class ProducerSingleton:
    _instance = None

    @classmethod
    def get_instance(cls, rabbitmq_manager: RabbitMQManager, queue_name: str):
        if cls._instance is None:
            cls._instance = Producer(rabbitmq_manager, queue_name=queue_name)
        return cls._instance