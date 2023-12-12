from fastapi import APIRouter, Form, File, UploadFile, status, Depends, Request
from app.repository.company.models.company_models import CompanyIn, CompanyOut, CompanyId, CompanyForm, ResLogin
from app.repository.company.sqlalchemy import CompanyRepository
from app.repository.company.controller import CompanyController
from app.repository.company.service import CompanyService
from app.utils.auth import get_authenticated_user
from typing import Any, Annotated
from sqlalchemy.orm import Session

repository = CompanyRepository()
service = CompanyService(repository)
controller = CompanyController(service)

router = APIRouter(prefix="/company", tags=["company"])

def get_db(request: Request):
    return request.state.db

@router.get('/{company_id}', status_code=status.HTTP_200_OK, response_model=CompanyOut)
def get_company_by_id(company_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    return controller.get_company_by_id_controller(company_id, session)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[CompanyOut])
def get_companies(current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    if current_user['role'] == 'admin':
        return controller.get_companies_controller(session)
    else:
        pass #retorno

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CompanyId)
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

@router.put('/{company_id}', status_code=status.HTTP_200_OK, response_model=CompanyOut)
def update_company(company_id: str, company: CompanyIn, session: Session = Depends(get_db)) -> Any:
    return controller.update_company_controller(company_id, company, session)

@router.delete('/{company_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_company(company_id: str, session: Session = Depends(get_db)) -> None:
    controller.delete_company_controller(company_id, session)
