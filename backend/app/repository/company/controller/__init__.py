from app.repository.company.exceptions import CompanyNotFoundError, CompanyControllerException
from app.repository.company.models.company_models import CompanyIn, CompanyOut, CompanyId
from app.repository.company.models.controller_interface import ICompanyController
from app.repository.company.models.service_interface import ICompanyService
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)

class CompanyController(ICompanyController):

    def __init__(self, service: ICompanyService):
        self._service = service

    def get_company_by_id_controller(self, company_id: str, session: Session) -> CompanyOut:
        try:
            return self._service.get_company_by_id_service(company_id, session)
        except CompanyNotFoundError as error:
            logger.error("Company not found: %s", error)
            raise
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise CompanyControllerException("Failed to fetch company by ID.") from error

    def get_companies_controller(self, session: Session) -> list[CompanyOut] | list:
        try:
            return self._service.get_companies_service(session)
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise CompanyControllerException("Failed to fetch companies.") from error

    def create_company_controller(
        self, 
        name: str,
        area: str,
        description: str,
        localization: str,
        session: Session
    ) -> CompanyId:
        try:
            return self._service.create_company_service(
                name,
                area,
                description,
                localization,
                session
            )
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise CompanyControllerException("Failed to create company.") from error

    def update_company_controller(self, company_id: str, company: CompanyIn, session: Session) -> CompanyOut:
        try:
            return self._service.update_company_service(company_id, company, session)
        except CompanyNotFoundError as error:
            logger.error("Company not found: %s", error)
            raise
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise CompanyControllerException("Failed to update company.") from error

    def delete_company_controller(self, company_id: str, session: Session) -> None:
        try:
            self._service.delete_company_service(company_id, session)
        except CompanyNotFoundError as error:
            logger.error("Company not found: %s", error)
            raise
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise CompanyControllerException("Failed to delete company.") from error
