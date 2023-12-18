from app.repository.dashboard.dashboard_model import PutDashboard, GetDashboardResponse, GetDashboardId, RegisterDashboardResponse
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod

class IDashboardService(ABC):

    @abstractmethod
    def get_dashboard_by_id_service(self, dashboard_id: str, session: Session) -> GetDashboardResponse:
        pass

    @abstractmethod
    def get_dashboards_service(self, session: Session) -> GetDashboardResponse:
        pass

    @abstractmethod
    def create_dashboard_service(
        self, 
        name: str,
        description: str,
        company_id: str,
        session: Session
    ) -> RegisterDashboardResponse:
        pass

    @abstractmethod
    def update_dashboard_service(self, dashboard_id: str, dashboard_updated: PutDashboard, session: Session) -> GetDashboardResponse:
        pass

    @abstractmethod
    def delete_dashboard_service(self, dashboard_id: str, session: Session) -> None:
        pass
