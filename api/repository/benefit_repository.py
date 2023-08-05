


from typing import List
from elasticsearch import NotFoundError
from api.repository.elasticsearch.repository_base import RepositoryBase
from api.schemas.cpf_data import CpfData



class BenefitRepository(RepositoryBase):
    async def get_cpf_data_by_cpf(self, cpf: str) -> List[CpfData]:
        try:
            query = {
                "query": 
                {
                    "match": 
                    {
                        "cpf": cpf
                    }
                }
            }

            results = await self.search_index(index="cpf_index", query=query)
            return [CpfData(**hit["_source"]) for hit in results["hits"]["hits"]]
        except NotFoundError:
            return []

    async def get_all_cpf_data(self, page: int, page_size: int) -> List[CpfData]:
        try:
            query = {
                "query": {
                    "match_all": {}
                }
            }
            from_ = page_size * (page - 1)
            results = await self.search_index(index="cpf_index", query=query, from_=from_, size=page_size)
            return [CpfData(**hit["_source"]) for hit in results["hits"]["hits"]]
        except NotFoundError:
            return []