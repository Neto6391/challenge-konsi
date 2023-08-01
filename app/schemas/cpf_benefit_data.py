
from pydantic import BaseModel
from typing import List


class CPFBenefitData(BaseModel):
    username: str
    password: str
    cpf: List[str]