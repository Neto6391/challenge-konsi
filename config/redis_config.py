import json

from redis import Redis
from config.logging import logger

class RedisCache:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connect(*args, **kwargs)
        return cls._instance

    def _connect(self, host, port, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.redis = None

    def initialize(self):
        try:
            self.redis = Redis(self.host, self.port, self.db)
            logger.info("Redis Connected!")
        except Exception as e:
            logger.error(f"Error connecting to Redis: {e}")
            raise
            

    def store_data(self, key, data):
        try:
            data_json = json.dumps(data)
            if self.redis is not None:
                self.redis.set(key, data_json)
            return True
        except Exception as e:
            print("Error storing data in Redis: ", e)
            return False

    def get_data(self, key):
        try:
            if self.redis is not None:
                data_json = self.redis.get(key)
            if data_json:
                data = json.loads(data_json)
                return data
            else:
                return None
        except Exception as e:
            print("Error getting data from Redis: ", e)
            return None
        
    def close(self):
        try:
            if self.redis is not None:
                self.redis.close()
                logger.info("Redis Desconnect!")
        except Exception as e:
            print("Something was happening: ", e)