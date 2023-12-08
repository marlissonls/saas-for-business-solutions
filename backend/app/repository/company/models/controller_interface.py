from app.repository.company.models.company_models import CompanyIn, CompanyOut, CompanyId
from abc import ABC, abstractmethod

class ICompanyController(ABC):

    @abstractmethod
    def get_company_by_id_controller(self, company_id: str) -> CompanyOut:
        pass

    @abstractmethod
    def get_companies_controller(self) -> list[CompanyOut]:
        pass

    @abstractmethod
    def create_company_controller(self, company: CompanyIn) -> CompanyId:
        pass

    @abstractmethod
    def update_company_controller(self, company_id: str, company: CompanyIn) -> CompanyOut:
        pass

    @abstractmethod
    def delete_company_controller(self, company_id: str) -> None:
        pass
