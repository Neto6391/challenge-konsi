from config.elastic_search_config import ElasticConfig


class ElasticConfigFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_elastic_config()
        return cls._instance

    def init_elastic_config(self):
        self.elastic_config = ElasticConfig()

    def get_instance(self):
        return self.elastic_config