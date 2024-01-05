from app.repository.dashboards.models.dashboard_model import GetDashboardResponse, RegisterDashboardResponse, PutDashboard
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod

class IDashboardController(ABC):

    @abstractmethod
    def get_dashboard_by_id_controller(self, dashboard_id: str, session: Session) -> GetDashboardResponse:
        pass
    
    @abstractmethod
    def get_dashboards_controller(self, session: Session) -> GetDashboardResponse:
        pass

    @abstractmethod
    def create_dashboard_controller(
        self, 
        name: str,
        description: str,
        company_id: str,
        session: Session
    ) -> RegisterDashboardResponse:
        pass

    @abstractmethod
    def update_dashboard_controller(self, dashboard_id: str, name: str, description: str,  dashboard: PutDashboard, session: Session) -> GetDashboardResponse:
        pass

    @abstractmethod
    def delete_dashboard_controller(self, dashboard_id: str, session: Session) -> GetDashboardResponse:
        pass
