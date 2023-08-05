from pydantic import BaseModel

class CpfData(BaseModel):
    cpf: str
    benefit: int