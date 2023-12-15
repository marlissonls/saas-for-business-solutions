from app.db.schema import Company
from app.repository.company.models.company_models import PutCompany
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import List


class ICompanyRepository(ABC):

    @abstractmethod
    def get_company_by_id_repository(self, company_id: str, session: Session) -> Company | None:
        pass

    @abstractmethod
    def get_companies_repository(self, session: Session) -> List[Company] | list:
        pass
    
    @abstractmethod
    def create_company_repository(self, company: Company, session: Session) -> None:
        pass

    @abstractmethod
    def update_company_repository(self, company: Company, session: Session) -> None:
        pass

    @abstractmethod
    def delete_company_repository(self, company: Company, session: Session) -> None:
        pass