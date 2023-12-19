from fastapi import Depends
from app.utils.auth import get_authenticated_user
from app.repository.dashboards.models.dashboard_model import PutDashboard, RegisterDashboardResponse, GetDashboardId, GetDashboardData, GetDashboardResponse
from app.repository.dashboards.models.dashboard_controller_interface import IDashboardController
from app.repository.dashboards.models.dashboard_service_interface import IDashboardService
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)

class DashboardController(IDashboardController):

    def __init__(self, service: IDashboardService):
        self._service = service

    def get_dashboard_by_id_controller(self, dashboard_id: str, session: Session) -> GetDashboardResponse:
        try:
            return self._service.get_dashboard_by_id_service(dashboard_id, session)
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def get_dashboards_controller(self, session: Session) -> GetDashboardResponse:
        try:
            return self._service.get_dashboards_service(session)
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def create_dashboard_controller(
        self,
        name: str,
        description: str,
        company_id: str,
        session: Session
    ) -> RegisterDashboardResponse:
        try:
            return self._service.create_dashboard_service(
                name,
                description,
                company_id,
                session
            )
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def update_dashboard_controller(
        self,
        dashboard_id: str,
        name: str,
        description: str,
        session: Session,
    ) -> GetDashboardResponse:
        try:
            return self._service.update_dashboard_service(
                dashboard_id,
                name,
                description,
                session
            )
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def delete_dashboard_controller(self, dashboard_id: str, session: Session) -> GetDashboardResponse:
        try:
            self._service.delete_dashboard_service(dashboard_id, session)
        except Exception as error:
            print('aqui esta',error)
            logger.error("An error occurred: %s", error)
