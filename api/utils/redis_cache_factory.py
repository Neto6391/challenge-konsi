import os
from config.environment import get_config
from config.redis_config import RedisCache


class RedisCacheFactory:
    @classmethod
    def get_instance(cls) -> RedisCache:
        config = get_config(os.environ.get('ENVIRONMENT'))
        redis_cache = RedisCache(config.REDIS_HOST, config.REDIS_PORT)
        return redis_cache