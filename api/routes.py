import os
from fastapi import APIRouter

from api.schemas.cpf_benefit_data import CPFBenefitData
from api.controllers.benefit_controller import BenefitController


router = APIRouter()
benefit_controller = BenefitController()

@router.post('/api/cpf/create')
async def create_benefit_by_cpf(data: CPFBenefitData):
    try:
        await benefit_controller.create_benefit_by_cpf(data)
    except Exception as e:
        raise ValueError(f'Something is happen {e}')