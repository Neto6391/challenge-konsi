from elasticsearch import AsyncElasticsearch
from elasticsearch.exceptions import RequestError
from config.logging import logger

class ElasticConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_connection()
        return cls._instance

    def init_connection(self):
        self.client = AsyncElasticsearch(['http://localhost:9200'])
        logger.info("ElasticSearch Connected!")

    async def close(self):
        await self.client.close()
        logger.info("Desconnect ElasticSearch!")

    def get_client(self):
        return self.client

    async def create_indice(self, index_name, mappings):
        try:
            is_indices_exists = await self.client.indices.exists(index=index_name)
            if not is_indices_exists:
                await self.client.indices.create(index=index_name, body=mappings)
                logger.info("Created Indice!")
            else:
                logger.info("Cached Indice!")
            return True
        except RequestError as e:
            logger.error(f'Error creating index: {e}')
            return False
    
    async def create_index(self, index: str, id: str, document: any):
        await self.client.index(index=index, id=id, document=document)
        logger.info("Document added in index!")

    async def search(self, index, query, from_, size):
        try:
            results = await self.client.search(index=index, body=query, from_=from_, size=size)
            return results
        except RequestError as e:
            logger.error(f'Error searching in Elasticsearch: {e}')
            return None
    

