
from app.schemas.cpf_benefit_data import CPFBenefitData

class BenefitService:

    def create_benefit_by_cpf(self, data: CPFBenefitData):
        return data