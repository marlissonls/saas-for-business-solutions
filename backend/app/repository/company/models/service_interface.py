from app.repository.company.models.company_models import PutCompany, GetCompanyResponse, GetCompanyId, RegisterCompanyResponse
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import List

class ICompanyService(ABC):

    @abstractmethod
    def get_company_by_id_service(self, company_id: str) -> GetCompanyResponse:
        pass

    @abstractmethod
    def get_companies_service(self) -> GetCompanyResponse:
        pass

    @abstractmethod
    def create_company_service(
        self, 
        name: str,
        area: str,
        localization: str,
        description: str,
        session: Session
    ) -> RegisterCompanyResponse:
        pass

    @abstractmethod
    def update_company_service(self, company_id: str, company_updated: PutCompany) -> GetCompanyResponse:
        pass

    @abstractmethod
    def delete_company_service(self, company_id: str) -> None:
        pass