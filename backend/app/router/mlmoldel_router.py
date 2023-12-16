from fastapi import APIRouter, Form, File, UploadFile, status, Depends, Request
from app.repository.company.models.company_models import PutCompany, GetCompanyResponse, RegisterCompanyResponse, GetCompanyData
from app.repository.company.sqlalchemy import CompanyRepository
from app.repository.company.controller import CompanyController
from app.repository.company.service import CompanyService
from app.utils.auth import get_authenticated_user
from typing import Any, Annotated, Optional
from sqlalchemy.orm import Session
import logging

repository = CompanyRepository()
service = CompanyService(repository)
controller = CompanyController(service)

router = APIRouter(prefix="/company", tags=["company"])

def get_db(request: Request):
    return request.state.db

@router.get('/{company_id}', status_code=status.HTTP_200_OK, response_model=GetCompanyResponse)
def get_company_by_id(company_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    if current_user['role'] == 'admin':
        return controller.get_company_by_id_controller(company_id, session)
    else:
        return GetCompanyResponse(
            status=False,
            message='Acesso negado.',
            data=None,
        )


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


@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=RegisterCompanyResponse)
def create_company(
    name: Annotated[str, Form()],
    area: Annotated[str, Form()],
    description: Annotated[str, Form()],
    localization: Annotated[str, Form()],
    session: Session = Depends(get_db)
) -> Any:
    return controller.create_company_controller(
        name,
        area,
        description,
        localization,
        session
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
    company_data = PutCompany(name=name, area=area, description=description, localization=localization)
    return controller.update_company_controller(company_id, company_data, session)

@router.delete('/{company_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_company(company_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> None:
    controller.delete_company_controller(company_id, session)