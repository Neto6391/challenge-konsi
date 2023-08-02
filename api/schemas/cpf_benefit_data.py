import re
from pydantic import BaseModel, constr, validator
from typing import List



class CPFBenefitData(BaseModel):
    username: constr(min_length=1)
    password: constr(min_length=1)
    cpf: List[constr(min_length=14)]

    @validator('cpf', each_item=True)
    def validate_cpf(cls, cpf):
        pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
        if not pattern.match(cpf):
            raise ValueError('CPF invalid. The correct format is XXX.XXX.XXX-XX.')
        return cpf