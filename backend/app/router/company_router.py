from app.repository.company.models.company_models import GetCompanyResponse, RegisterCompanyResponse
from app.repository.company.sqlalchemy import CompanyRepository
from app.repository.company.controller import CompanyController
from app.repository.company.service import CompanyService
from app.utils.auth import get_authenticated_user
from fastapi import APIRouter, status, Form, Depends, Request
from typing import Any, Annotated, Optional
from sqlalchemy.orm import Session

repository = CompanyRepository()
service = CompanyService(repository)
controller = CompanyController(service)

router = APIRouter(prefix="/company", tags=["company"])

def get_db(request: Request):
    return request.state.db

@router.get('/{company_id}', status_code=status.HTTP_200_OK, response_model=GetCompanyResponse)
def get_company_by_id(company_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    return controller.get_company_by_id_controller(company_id, session)


@router.get('/', status_code=status.HTTP_200_OK, response_model=GetCompanyResponse)
def get_companies(current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    if current_user['role'] == 'admin':
        return controller.get_companies_controller(session)
    else:
        return GetCompanyResponse(
            status=False,
            message='Acesso negado.',
            data=None,
        )


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=RegisterCompanyResponse)
def create_company(
    name: Annotated[str, Form()],
    area: Annotated[str, Form()],
    description: Annotated[str, Form()],
    localization: Annotated[str, Form()],
    current_user: dict = Depends(get_authenticated_user),
    session: Session = Depends(get_db)
) -> Any:
    if current_user['role'] == 'admin':
        return controller.create_company_controller(
            name,
            area,
            description,
            localization,
            session
        )
    else:
        return RegisterCompanyResponse(
            status=False,
            message='Acesso negado.',
            data=None,
        )

@router.put('/{company_id}', status_code=status.HTTP_200_OK, response_model=GetCompanyResponse)
def update_company(
    company_id: str,
    name: Optional[str] = Form(None),
    area: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    localization: Optional[str] = Form(None),
    current_user: dict = Depends(get_authenticated_user),
    session: Session = Depends(get_db)
) -> Any:
    if current_user['role'] == 'admin':
        return controller.update_company_controller(
            company_id, 
            name,
            area,
            description,
            localization,
            session
        )
    else:
        return GetCompanyResponse(
            status=False,
            message='Acesso negado.',
            data=None,
        )

@router.delete('/{company_id}', status_code=status.HTTP_200_OK, response_model=GetCompanyResponse)
def delete_company(company_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    if current_user['role'] == 'admin':
        return controller.delete_company_controller(company_id, session)
    else:
        return GetCompanyResponse(
            status=False,
            message='Acesso negado.',
            data=None,
        )