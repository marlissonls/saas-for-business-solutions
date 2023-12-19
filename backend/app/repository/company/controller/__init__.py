from app.repository.company.models.company_models import RegisterCompanyResponse, GetCompanyResponse
from app.repository.company.models.controller_interface import ICompanyController
from app.repository.company.models.service_interface import ICompanyService
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)

class CompanyController(ICompanyController):

    def __init__(self, service: ICompanyService):
        self._service = service

    def get_company_by_id_controller(self, company_id: str, session: Session) -> GetCompanyResponse:
        try:
            return self._service.get_company_by_id_service(company_id, session)
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def get_companies_controller(self, session: Session) -> GetCompanyResponse:
        try:
            return self._service.get_companies_service(session)
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def create_company_controller(
        self,
        name: str,
        area: str,
        description: str,
        localization: str,
        session: Session
    ) -> RegisterCompanyResponse:
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

    def update_company_controller(
        self,
        company_id: str,
        name: str,
        area: str,
        description: str,
        localization: str,
        session: Session, 
    ) -> GetCompanyResponse:
        try:
            return self._service.update_company_service(
                company_id,
                name,
                area,
                description,
                localization,
                session
            )
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def delete_company_controller(self, company_id: str, session: Session) -> GetCompanyResponse:
        try:
            return self._service.delete_company_service(company_id, session)
        except Exception as error:
            logger.error("An error occurred: %s", error)
