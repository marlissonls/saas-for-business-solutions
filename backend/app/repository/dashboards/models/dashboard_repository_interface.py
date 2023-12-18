from app.db.schema import Dashboard
from app.repository.dashboard.dashboard_model import PutDashboard
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import List


class IDashboardRepository(ABC):

    @abstractmethod
    def get_dashboard_by_id_repository(self, dashboard_id: str, session: Session) -> Dashboard | None:
        pass

    @abstractmethod
    def get_dashboards_repository(self, session: Session) -> List[Dashboard] | list:
        pass
    
    @abstractmethod
    def create_dashboard_repository(self, dashboard: Dashboard, session: Session) -> None:
        pass

    @abstractmethod
    def update_dashboard_repository(self, dashboard: Dashboard, session: Session) -> None:
        pass

    @abstractmethod
    def delete_dashboard_repository(self, dashboard: Dashboard, session: Session) -> None:
        pass
