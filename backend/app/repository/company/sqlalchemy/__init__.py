from app.repository.company.models.repository_interface import ICompanyRepository
from app.db.schema import Company
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List


class CompanyRepository(ICompanyRepository):

    def get_company_by_id_repository(self, company_id: str, session: Session) -> Company | None:
        return session.query(Company).filter(and_(Company.id == company_id, Company.deleted_at == None)).first()

    def get_companies_repository(self, session: Session) -> List[Company] | List:
        return session.query(Company).filter(Company.deleted_at == None).all()

    def create_company_repository(self, company: Company, session: Session) -> None:
        session.add(company)

    def update_company_repository(self, company: Company, session: Session) -> None:
        session.merge(company)

    def delete_company_repository(self, company: Company, session: Session) -> None:
        session.merge(company)

