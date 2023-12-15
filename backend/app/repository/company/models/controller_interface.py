from app.repository.company.models.company_models import GetCompanyResponse, RegisterCompanyResponse, PutCompany
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod

class ICompanyController(ABC):

    @abstractmethod
    def get_company_by_id_controller(self, company_id: str, session: Session) -> GetCompanyResponse:
        pass
    
    @abstractmethod
    def get_companies_controller(self, session: Session) -> GetCompanyResponse:
        pass

    @abstractmethod
    def create_company_controller(
        self, 
        name: str,
        area: str,
        description: str,
        localization: str,
        session: Session
    ) -> RegisterCompanyResponse:
        pass

    @abstractmethod
    def update_company_controller(self, company_id: str, company: PutCompany, session: Session) -> GetCompanyResponse:
        pass

    @abstractmethod
    def delete_company_controller(self, company_id: str, session: Session) -> GetCompanyResponse:
        pass
