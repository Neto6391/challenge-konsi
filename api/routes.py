from fastapi import APIRouter, Depends
from api.schemas.cpf_benefit_data import CPFBenefitData
from api.controllers.benefit_controller import BenefitController
from api.utils.rabbitmq_manager_singleton import RabbitMQManagerSingleton
from config.rabbitmq_manager import RabbitMQManager

router = APIRouter()

@router.post('/api/cpf/create')
async def create_benefit_by_cpf(data: CPFBenefitData, rabbitmq_manager_singleton: RabbitMQManagerSingleton = Depends(RabbitMQManagerSingleton)):
    try:
        benefit_controller = BenefitController(rabbitmq_manager_singleton.get_rabbitmq_manager())
        await benefit_controller.create_benefit_by_cpf(data)
        return None
    except Exception as e:
        raise ValueError(f'Something is happen {e}')
