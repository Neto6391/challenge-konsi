from fastapi import APIRouter, Depends
from api.repository.benefit_repository import BenefitRepository
from api.schemas.cpf_benefit_data import CPFBenefitData
from api.controllers.benefit_controller import BenefitController
from api.schemas.query_params_data import QueryParamsData
from api.utils.rabbitmq_manager_singleton import RabbitMQManagerSingleton
from api.utils.redis_cache_factory import RedisCacheFactory
from config.logging import logger

router = APIRouter()

@router.post('/api/cpf/create')
async def create_benefit_by_cpf(data: CPFBenefitData, rabbitmq_manager_singleton: RabbitMQManagerSingleton = Depends(RabbitMQManagerSingleton), redis_cache: RedisCacheFactory = Depends(RedisCacheFactory), benefit_repository: BenefitRepository = Depends(BenefitRepository)):
    try:
        benefit_controller = BenefitController(benefit_repository, rabbitmq_manager_singleton.get_rabbitmq_manager(), redis_cache.get_instance())
        await benefit_controller.create_benefit_by_cpf(data)
        return "Ok"
    except Exception as e:
        raise ValueError(f'Something is happen {e}')
    
@router.get('/api/cpf')
async def create_benefit_by_cpf(params: QueryParamsData = Depends(), benefit_repository: BenefitRepository = Depends(BenefitRepository)):
    try:
        benefit_controller = BenefitController(benefit_repository)
        logger.info(f"Data ${params.cpf} - {params.page} - {params.page_size}")
        if params.cpf:
            return await benefit_controller.get_cpf_data_by_cpf(cpf=params.cpf)
        else:
            
            return await benefit_controller.get_all_cpf_data(page=params.page, page_size=params.page_size)
    except Exception as e:
        raise ValueError(f'Something is happen {e}')
