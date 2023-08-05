from api.utils.elastic_search_factory import ElasticConfigFactory
from config.elastic_search_config import ElasticConfig
from config.logging import logger


class RepositoryBase:
    def __init__(self):
        self.client: ElasticConfig = ElasticConfigFactory().get_instance()

    async def index_document(self, index_name, id, data):
        try:
            result = await self.client.create_index(index=index_name, id=id, document=data)
            return result
        except Exception as e:
            logger.error(f'Error indexing document: {e}')
            return None
        
    async def search_index(self, index, query, from_=None, size=None):
        try:
            results = await self.client.search(index=index, query=query, from_=from_, size=size)
            return results
        except Exception as e:
            logger.error(f'Error searching in Elasticsearch: {e}')
            return None

