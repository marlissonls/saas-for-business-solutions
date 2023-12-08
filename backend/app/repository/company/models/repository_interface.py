from app.db.schema import Company
from app.repository.company.models.company_models import CompanyIn
from sqlalchemy.orm import Session as SQLAlchemySession
from abc import ABC, abstractmethod
from typing import List


class ICompanyRepository(ABC):

    @abstractmethod
    def get_company_by_id_repository(self, client: SQLAlchemySession, company_id: str) -> Company | None:
        pass

    @abstractmethod
    def get_companies_repository(self, client: SQLAlchemySession) -> List[Company]:
        pass
    
    @abstractmethod
    def create_company_repository(self, client: SQLAlchemySession, company: CompanyIn) -> None:
        pass

    @abstractmethod
    def update_company_repository(self, client: SQLAlchemySession, company: Company) -> None:
        pass

    @abstractmethod
    def delete_company_repository(self, client: SQLAlchemySession, company: Company) -> None:
        pass
