from api.utils.elastic_search_factory import ElasticConfigFactory
from config.elastic_search_config import ElasticConfig


class RepositoryBase:
    def __init__(self):
        self.client: ElasticConfig = ElasticConfigFactory().get_instance()

    async def index_document(self, index_name, id, data):
        try:
            result = await self.client.create_index(index=index_name, id=id, document=data)
            return result
        except Exception as e:
            print("Error indexing document: ", e)
            return None

