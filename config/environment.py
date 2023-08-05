from dotenv import load_dotenv
import os


class Config:
    _instance = None

    def __new__(cls, environment):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config(environment)
        return cls._instance

    def _load_config(self, environment):
        load_dotenv(f".env.{environment}")
        self.ENVIRONMENT = os.environ.get('ENVIRONMENT', 'development')
        self.REDIS_HOST = os.environ.get('REDIS_HOST')
        self.REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
        self.RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
        self.RABBITMQ_PORT = int(os.environ.get('RABBITMQ_PORT', 5672))
        self.RABBITMQ_USER = os.environ.get('RABBITMQ_USER')
        self.RABBITMQ_PASS = os.environ.get('RABBITMQ_PASS')
        self.RABBITMQ_VHOST = os.environ.get('RABBITMQ_VHOST', '/')

    def get_redis_config(self):
        return {
            'host': self.REDIS_HOST,
            'port': self.REDIS_PORT
        }

    def get_rabbitmq_config(self):
        return {
            'host': self.RABBITMQ_HOST,
            'port': self.RABBITMQ_PORT,
            'user': self.RABBITMQ_USER,
            'pass': self.RABBITMQ_PASS,
            'vhost': self.RABBITMQ_VHOST
        }

    def is_redis_config_defined(self):
        return self.REDIS_HOST is not None and self.REDIS_PORT is not None

    def is_rabbitmq_config_defined(self):
        return (
            self.RABBITMQ_HOST is not None
            and self.RABBITMQ_PORT is not None
            and self.RABBITMQ_USER is not None
            and self.RABBITMQ_PASS is not None
        )

class DevelopmentConfig(Config):
    pass

class HomologConfig(Config):
    pass

class ProductionConfig(Config):
    pass

CONFIG_MAP = {
    'development': DevelopmentConfig,
    'homolog': HomologConfig,
    'production': ProductionConfig
}

def get_config(environment):
    config_class = CONFIG_MAP.get(environment, DevelopmentConfig)
    return config_class(environment)
