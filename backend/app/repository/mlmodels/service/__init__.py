from app.repository.mlmodels.models.model_models import PutModel, RegisterModelResponse, GetModelId, GetModelData, GetModelResponse
from app.repository.mlmodels.models.model_repository_interface import IModelRepository
from app.repository.mlmodels.models.model_service_interface import IModelService
from app.db.schema import Model
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import UploadFile
from uuid import uuid1
from datetime import datetime, timedelta

class ModelService(IModelService):

    def __init__(self, repository: IModelRepository):
        self._repository = repository

    def get_model_by_id_service(self, model_id: str, session: Session) -> GetModelResponse:
        try:
            model = self._repository.get_model_by_id_repository(model_id, session)

            if not model:
                return GetModelResponse(
                    status=False,
                    message='Não foi possível encontrar este modelo.',
                    data=None
                )

            return GetModelResponse(
                status=True,
                message='Modelo encontrado com sucesso.',
                data=GetModelData(
                    id=model.id,
                    name=model.name,
                    description=model.description,
                    company_id=model.company_id
                )
            )

        except Exception as error:
            session.rollback()
            return GetModelResponse(
                status=False,
                message=f'Erro interno no servidor',
                data=None
            )

    def get_models_service(self, session: Session) -> GetModelResponse:
        try:
            models = self._repository.get_models_repository(session)

            if not models:
                return GetModelResponse(
                    status=True,
                    message='Nenhum modelo encontrado nesta pesquisa.',
                    data=[]
                )

            models_data_list = [GetModelData(id=model.id, name=model.name, description=model.description, company_id=model.company_id) for model in models]
            return GetModelResponse(
                status=True,
                message='Modelos encontrados com sucesso.',
                data=models_data_list
            )

        except Exception as error:
            session.rollback()
            return GetModelResponse(
                status=False,
                message='Erro interno no servidor.',
                data=None
            )

    def create_model_service(
        self, 
        name: str,
        description: str,
        company_id: str,
        session: Session
    ) -> RegisterModelResponse:
        try:
            new_model_id = str(uuid1())

            new_model = Model(
                id=new_model_id,
                name=name,
                description=description,
                company_id=company_id
            )

            self._repository.create_model_repository(new_model, session)

            session.commit()

            return RegisterModelResponse(
                status=True,
                message=f"Modelo {name} cadastrado com sucesso.",
                data=GetModelId(id=new_model.id)
            )

        except Exception as error:
            session.rollback()
            return RegisterModelResponse(
                status=False,
                message=f"Erro ao cadastrar este modelo.",
                data=None
            )

    def update_model_service(
        self, 
        model_id: str, 
        name: str,
        description: str,
        session: Session,
    ) -> GetModelResponse:
        try:
            model = self._repository.get_model_by_id_repository(model_id, session)

            if not model:
                return GetModelResponse(
                    status=False,
                    message='Não foi possível encontrar este modelo.',
                    data=None
                )

            if name: model.name=name
            if description: model.description=description
            model.updated_at = datetime.utcnow()

            self._repository.update_model_repository(model, session)

            session.commit()

            return GetModelResponse(
                status=True,
                message='Dados do modelo atualizados.',
                data=GetModelData(
                    id=model.id,
                    name=model.name,
                    description=model.description,
                    company_id=model.company_id
                )
            )
        except Exception as error:
            session.rollback()
            return GetModelResponse(
                status=False,
                message='Erro interno no servidor.',
                data=None
            )

    def delete_model_service(self, model_id: str, session: Session) -> GetModelResponse:
        try:
            model = self._repository.get_model_by_id_repository(model_id, session)

            if not model:
                return GetModelResponse(
                    status=False,
                    message='Não foi possível encontrar este modelo.',
                    data=None
                )
            
            model.deleted_at = datetime.utcnow()

            self._repository.delete_model_repository(model, session)

            session.commit()

            return GetModelResponse(
                status=True,
                message='Modelo deletado.',
                data=None
            )

        except Exception as error:
            session.rollback()
            return GetModelResponse(
                status=False,
                message='Erro interno no servidor.',
                data=None
            )
