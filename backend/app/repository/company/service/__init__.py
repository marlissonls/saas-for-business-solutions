from app.repository.company.models.company_models import RegisterCompanyResponse, GetCompanyResponse, GetCompanyId, GetCompanyData
from app.repository.company.models.repository_interface import ICompanyRepository
from app.repository.company.models.service_interface import ICompanyService
from app.db.schema import Company
from sqlalchemy.orm import Session
from uuid import uuid1
from datetime import datetime, timedelta


class CompanyService(ICompanyService):

    def __init__(self, repository: ICompanyRepository):
        self._repository = repository

    def get_company_by_id_service(self, company_id: str, session: Session) -> GetCompanyResponse:
        try:
            company = self._repository.get_company_by_id_repository(company_id, session)

            if not company:
                return GetCompanyResponse(
                    status=False,
                    message='Empresa não encontrada.',
                    data=None
                )

            return GetCompanyResponse(
                status=True,
                message='Empresa encontrada com sucesso.',
                data=GetCompanyData(
                    id=company.id,
                    name=company.name,
                    area=company.area,
                    description=company.description,
                    localization=company.localization,
                    phone=company.phone
                )
            )

        except Exception as error:
            session.rollback()
            return GetCompanyResponse(
                status=False,
                message=f'500: Erro interno no servidor',
                data=None
            )

    def get_companies_service(self, session: Session) -> GetCompanyResponse:
        try:
            companies = self._repository.get_companies_repository(session)

            if not companies:
                return GetCompanyResponse(
                    status=True,
                    message='Nenhuma empresa encontrada nesta pesquisa.',
                    data=[]
                )
            
            companies_data_list = [GetCompanyData(id=company.id, name=company.name, area=company.area, description=company.description, localization=company.localization, phone=company.phone) for company in companies]
            return GetCompanyResponse(
                status=True,
                message='Empresas encontradas com sucesso.',
                data=companies_data_list
            )

        except Exception as error:
            session.rollback()
            return GetCompanyResponse(
                status=False,
                message='500: Erro interno no servidor',
                data=None
            )

    def create_company_service(
        self, 
        name: str,
        area: str,
        description: str,
        localization: str,
        phone: str,
        session: Session
    ) -> RegisterCompanyResponse:
        try:
            new_company_id = str(uuid1())

            new_company = Company(
                id=new_company_id,
                name=name,
                area=area,
                description=description,
                localization=localization,
                phone=phone
            )

            self._repository.create_company_repository(new_company, session)

            session.commit()

            return RegisterCompanyResponse(
                status=True,
                message=f"Empresa {name} cadastrada com sucesso.",
                data=GetCompanyId(id=new_company.id)
            )

        except Exception as error:
            session.rollback()
            return RegisterCompanyResponse(
                status=False,
                message=f"500: Erro interno no servidor.",
                data=None
            )

    def update_company_service(
        self, company_id: str, 
        name: str,
        area: str,
        description: str,
        localization: str,
        phone: str,
        session: Session) -> GetCompanyResponse:
        try:
            company = self._repository.get_company_by_id_repository(company_id, session)

            if not company:
                return GetCompanyResponse(
                    status=False,
                    message='Empresa não encontrada.',
                    data=None
                )

            if name: company.name = name
            if area: company.area = area
            if description: company.description = description
            if localization: company.localization = localization
            if phone: company.phone = phone
            company.updated_at = datetime.utcnow() + timedelta(hours=-3)

            self._repository.update_company_repository(company, session)

            session.commit()

            return GetCompanyResponse(
                status=True,
                message='Dados da empresa atualizados.',
                data=GetCompanyData(
                    id=company.id,
                    name=company.name,
                    area=company.area,
                    description=company.description,
                    localization=company.localization,
                    phone=company.phone
                )
            )
        except Exception as error:
            session.rollback()
            return GetCompanyResponse(
                status=False,
                message='500: Erro interno no servidor',
                data=None
            )

    def delete_company_service(self, company_id: str, session: Session) -> GetCompanyResponse:
        try:
            company = self._repository.get_company_by_id_repository(company_id, session)

            if not company:
                return GetCompanyResponse(
                    status=False,
                    message='Empresa não encontrada.',
                    data=None
                )
            
            company.deleted_at = datetime.utcnow()+timedelta(hours=-3)

            self._repository.delete_company_repository(company, session)

            session.commit()

            return GetCompanyResponse(
                status=True,
                message='Empresa desativada com sucesso.',
                data=None
            )

        except Exception as error:
            session.rollback()
            return GetCompanyResponse(
                status=False,
                message='500: Erro interno no servidor',
                data=None
            )
