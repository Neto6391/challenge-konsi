import os
from fastapi import APIRouter

from app.schemas.cpf_benefit_data import CPFBenefitData
from app.controllers.benefit_controller import BenefitController


router = APIRouter()
benefit_controller = BenefitController()

@router.post('/api/cpf/create')
def create_benefit_by_cpf(data: CPFBenefitData):
    return benefit_controller.create_benefit_by_cpf(data)