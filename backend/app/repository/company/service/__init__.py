from app.repository.company.exceptions import CompanyNotFoundError, InternalServerError
from app.repository.company.models.company_models import CompanyIn, CompanyOut, CompanyId
from app.repository.company.models.repository_interface import ICompanyRepository
from app.repository.company.models.service_interface import ICompanyService
from app.db.schema import Company
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import UploadFile
from uuid import uuid1

class CompanyService(ICompanyService):

    def __init__(self, repository: ICompanyRepository):
        self._repository = repository

    def get_company_by_id_service(self, company_id: str, session: Session) -> CompanyOut:
        try:
            company = self._repository.get_company_by_id_repository(company_id, session)

            if not company:
                raise CompanyNotFoundError(id=company_id)
            
            return CompanyOut(
                id=company.id,
                name=company.name,
                description =company.description 
            )

        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except Exception as error:
            raise InternalServerError(f"Internal Server Error: {str(error)}") from error

    def get_companies_service(self, session: Session) -> list[CompanyOut] | list:
        try:
            companies = self._repository.get_companies_repository(session)

            if not companies:
                return []
            
            return [CompanyOut(id=company.id, name=company.name, description =company.description ) for company in companies]

        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except Exception as error:
            raise InternalServerError(f"Internal Server Error: {str(error)}") from error

    def create_company_service(
        self, 
        name: str,
        description : str,
        session: Session
    ) -> CompanyId:
        try:
            new_company_id = str(uuid1())

            new_company = Company(
                id=new_company_id,
                name=name,
                description =description 
            )

            self._repository.create_company_repository(new_company, session)

            session.commit()

            return CompanyId(id=new_company.id)

        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error

    def update_company_service(self, company_id: str, company_updated: CompanyIn, session: Session) -> CompanyOut:
        try:
            company = self._repository.get_company_by_id_repository(company_id, session)

            if not company:
                raise CompanyNotFoundError(id=company_id)

            company.name = company_updated.name
            company.description  = company_updated.description 

            self._repository.update_company_repository(company, session)

            session.commit()

            return CompanyOut(
                id=company.id,
                name=company.name,
                description =company.description 
            )
        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error

    def delete_company_service(self, company_id: str, session: Session) -> None:
        try:
            company = self._repository.get_company_by_id_repository(company_id, session)

            if not company:
                raise CompanyNotFoundError(id=company_id)

            self._repository.delete_company_repository(company, session)

            session.commit()

        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
