from fastapi import APIRouter, status, Request, Depends, Form
from app.repository.dashboards.models.dashboard_model import PutDashboard, GetDashboardResponse, RegisterDashboardResponse
from app.repository.dashboards.sqlalchemy import DashboardRepository
from app.repository.dashboards.controller import DashboardController
from app.repository.dashboards.service import DashboardService
from app.utils.auth import get_authenticated_user
from sqlalchemy.orm import Session
from typing import Any, Annotated, Optional

repository = DashboardRepository()
service = DashboardService(repository)
controller = DashboardController(service)

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

def get_db(request: Request):
    return request.state.db

@router.get('/{dashboard_id}', status_code=status.HTTP_200_OK, response_model=GetDashboardResponse)
def get_dashboard_by_id(dashboard_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    return controller.get_dashboard_by_id_controller(dashboard_id, session)

@router.get('/', status_code=status.HTTP_200_OK, response_model=GetDashboardResponse)
def get_dashboards(current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    return controller.get_dashboards_controller(session)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=RegisterDashboardResponse)
def create_dashboard(
    name: Annotated[str, Form()],
    description: Annotated[str, Form()],
    company_id: Annotated[str, Form()],
    current_user: dict = Depends(get_authenticated_user),
    session: Session = Depends(get_db)
) -> Any:
    return controller.create_dashboard_controller(
        name,
        description,
        company_id,
        session
    )

@router.put('/{dashboard_id}', status_code=status.HTTP_200_OK, response_model=GetDashboardResponse)
def update_dashboard(
    dashboard_id: str,
    name: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    current_user: dict = Depends(get_authenticated_user),
    session: Session = Depends(get_db)
) -> Any:
    return controller.update_dashboard_controller(
        dashboard_id,
        name,
        description,
        session
    )

@router.delete('/{dashboard_id}', status_code=status.HTTP_200_OK, response_model=GetDashboardResponse)
def delete_dashboard(dashboard_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    if current_user['role'] == 'admin':
        return controller.delete_dashboard_controller(dashboard_id, session)
    else:
        return GetDashboardResponse(
            status=False,
            message='Acesso negado.',
            data=None,
        )
