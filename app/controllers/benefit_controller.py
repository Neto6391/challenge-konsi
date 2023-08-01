from app.schemas.cpf_benefit_data import CPFBenefitData
from app.services.benefit_service import BenefitService

class BenefitController:
    benefit_service = BenefitService()

    def create_benefit_by_cpf(self, data: CPFBenefitData):
        return self.benefit_service.create_benefit_by_cpf(data)