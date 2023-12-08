from app.repository.company.models.company_models import CompanyIn, CompanyOut, CompanyId
from abc import ABC, abstractmethod
from typing import List

class ICompanyService(ABC):

    @abstractmethod
    def get_company_by_id_service(self, company_id: str) -> CompanyOut:
        pass

    @abstractmethod
    def get_companies_service(self) -> List[CompanyOut]:
        pass

    @abstractmethod
    def create_company_service(self, company: CompanyIn) -> CompanyId:
        pass

    @abstractmethod
    def update_company_service(self, company_id: str, company_updated: CompanyIn) -> CompanyOut:
        pass

    @abstractmethod
    def delete_company_service(self, company_id: str) -> None:
        pass
