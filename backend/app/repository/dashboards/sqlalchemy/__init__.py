from app.repository.dashboard.dashboard_repository_interface import IDashboardRepository
from app.db.schema import Dashboard
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List


class DashboardRepository(IDashboardRepository):

    def get_dashboard_by_id_repository(self, dashboard_id: str, session: Session) -> Dashboard | None:
        return session.query(Dashboard).filter(and_(Dashboard.id == dashboard_id, Dashboard.deleted_at == None)).first()

    def get_dashboards_repository(self, session: Session) -> List[Dashboard] | List:
        return session.query(Dashboard).filter(Dashboard.deleted_at == None).all()

    def create_dashboard_repository(self, dashboard: Dashboard, session: Session) -> None:
        session.add(dashboard)

    def update_dashboard_repository(self, dashboard: Dashboard, session: Session) -> None:
        session.merge(dashboard)

    def delete_dashboard_repository(self, dashboard: Dashboard, session: Session) -> None:
        session.merge(dashboard)


