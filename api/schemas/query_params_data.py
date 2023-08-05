import re
from fastapi import Query
from pydantic import BaseModel
from typing import Optional



class QueryParamsData(BaseModel):
    cpf: Optional[str] = Query(None, description="CPF to filter by")
    page: int = Query(1, description="Page number")
    page_size: int = Query(10, description="Number of items per page")