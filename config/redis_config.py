import json
import aioredis

class RedisCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db

    async def _connect(self):
        self.redis = await aioredis.create_redis_pool(f'redis://{self.host}:{self.port}/{self.db}')

    async def store_data(self, key, data):
        try:
            data_json = json.dumps(data)
            if not hasattr(self, 'redis'):
                await self._connect()
            await self.redis.set(key, data_json)
            return True
        except Exception as e:
            print("Error storing data in Redis: ", e)
            return False

    async def get_data(self, key):
        try:
            if not hasattr(self, 'redis'):
                await self._connect()
            data_json = await self.redis.get(key)
            if data_json:
                data = json.loads(data_json)
                return data
            else:
                return None
        except Exception as e:
            print("Error getting data from Redis: ", e)
            return None
        
    async def close(self):
        try:
            if hasattr(self, 'redis'):
                self.redis.close()
                await self.redis.wait_closed()
        except Exception as e:
            print("Something was happening: ", e)