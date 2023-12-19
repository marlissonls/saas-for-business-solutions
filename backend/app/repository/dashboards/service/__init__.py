from app.repository.dashboards.models.dashboard_model import RegisterDashboardResponse, GetDashboardId, GetDashboardData, GetDashboardResponse
from app.repository.dashboards.models.dashboard_repository_interface import IDashboardRepository
from app.repository.dashboards.models.dashboard_service_interface import IDashboardService
from app.db.schema import Dashboard
from sqlalchemy.orm import Session
from uuid import uuid1
from datetime import datetime, timedelta

class DashboardService(IDashboardService):

    def __init__(self, repository: IDashboardRepository):
        self._repository = repository

    def get_dashboard_by_id_service(self, dashboard_id: str, session: Session) -> GetDashboardResponse:
        try:
            dashboard = self._repository.get_dashboard_by_id_repository(dashboard_id, session)

            if not dashboard:
                return GetDashboardResponse(
                    status=False,
                    message='Não foi possível encontrar este dashboard.',
                    data=None
                )

            return GetDashboardResponse(
                status=True,
                message='Dashboard encontrado com sucesso.',
                data=GetDashboardData(
                    id=dashboard.id,
                    name=dashboard.name,
                    description=dashboard.description,
                    company_id=dashboard.company_id
                )
            )

        except Exception as error:
            session.rollback()
            return GetDashboardResponse(
                status=False,
                message=f'500: Erro interno no servidor',
                data=None
            )

    def get_dashboards_service(self, session: Session) -> GetDashboardResponse:
        try:
            dashboards = self._repository.get_dashboards_repository(session)

            if not dashboards:
                return GetDashboardResponse(
                    status=True,
                    message='Nenhum dashboard encontrado nesta pesquisa.',
                    data=[]
                )

            dashboards_data_list = [GetDashboardData(id=dashboard.id, name=dashboard.name, description=dashboard.description, company_id=dashboard.company_id) for dashboard in dashboards]
            return GetDashboardResponse(
                status=True,
                message='Dashboards encontrados com sucesso.',
                data=dashboards_data_list
            )

        except Exception as error:
            session.rollback()
            return GetDashboardResponse(
                status=False,
                message=f'500: Erro interno no servidor',
                data=None
            )

    def create_dashboard_service(
        self, 
        name: str,
        description: str,
        company_id: str,
        session: Session
    ) -> RegisterDashboardResponse:
        try:
            new_dashboard_id = str(uuid1())

            new_dashboard = Dashboard(
                id=new_dashboard_id,
                name=name,
                description=description,
                company_id=company_id
            )

            self._repository.create_dashboard_repository(new_dashboard, session)

            session.commit()

            return RegisterDashboardResponse(
                status=True,
                message=f"Dashboard {name} cadastrado com sucesso.",
                data=GetDashboardId(id=new_dashboard.id)
            )

        except Exception as error:
            session.rollback()
            return RegisterDashboardResponse(
                status=False,
                message=f"Erro ao cadastrar este dashboard: {error}",
                data=None
            )

    def update_dashboard_service(
        self, 
        dashboard_id: str, 
        name: str,
        description: str,
        session: Session,
    ) -> GetDashboardResponse:
        try:
            dashboard = self._repository.get_dashboard_by_id_repository(dashboard_id, session)

            if not dashboard:
                return GetDashboardResponse(
                    status=False,
                    message='Não foi possível encontrar este dashboard.',
                    data=None
                )

            if name: dashboard.name=name
            if description: dashboard.description=description
            dashboard.updated_at = datetime.utcnow() + timedelta(hours=-3)

            self._repository.update_dashboard_repository(dashboard, session)

            session.commit()

            return GetDashboardResponse(
                status=True,
                message='Dados do dashboard atualizados.',
                data=GetDashboardData(
                    id=dashboard.id,
                    name=dashboard.name,
                    description=dashboard.description,
                    company_id=dashboard.company_id
                )
            )

        except Exception as error:
            session.rollback()
            return GetDashboardResponse(
                status=False,
                message=f'500: Erro interno no servidor',
                data=None
            )

    def delete_dashboard_service(self, dashboard_id: str, session: Session) -> GetDashboardResponse:
        try:
            dashboard = self._repository.get_dashboard_by_id_repository(dashboard_id, session)

            if not dashboard:
                return GetDashboardResponse(
                    status=False,
                    message='Não foi possível encontrar este dashboard.',
                    data=None
                )
            
            dashboard.deleted_at = datetime.utcnow()

            self._repository.delete_dashboard_repository(dashboard, session)

            session.commit()

            return GetDashboardResponse(
                status=True,
                message='Dashboard desativado.',
                data=None
            )

        except Exception as error:
            session.rollback()
            return GetDashboardResponse(
                status=False,
                message=f'500: Erro interno no servidor',
                data=None
            )
