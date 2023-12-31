from app.repository.mlmodels.interfaces.model_interface import RegisterModelResponse, GetModelId, GetModelData, GetModelResponse
from app.repository.mlmodels.interfaces.model_repository_interface import IModelRepository
from app.repository.mlmodels.interfaces.model_service_interface import IModelService
from app.db.schema import Model
from sqlalchemy.orm import Session
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
                    date=model.updated_at.strftime("%d/%m/%Y") if model.updated_at else model.created_at.strftime("%d/%m/%Y"),
                    description=model.description,
                    company_id=model.company_id,
                    features_inputs=model.features_inputs,
                    features_template=model.features_template,
                )
            )

        except Exception as error:
            print('OLHA AQUI EMBAIXO SEU ANIMAL')
            print(error)
            session.rollback()
            return GetModelResponse(
                status=False,
                message=f'Erro interno no servidor',
                data=None
            )

    def get_models_service(self, company_id: str, session: Session) -> GetModelResponse:
        try:
            models = self._repository.get_models_repository(company_id, session)

            if not models:
                return GetModelResponse(
                    status=True,
                    message='Nenhum modelo encontrado nesta pesquisa.',
                    data=[]
                )

            models_data_list = [
                GetModelData(
                    id=model.id,
                    name=model.name,
                    date=model.updated_at.strftime("%d/%m/%Y") if model.updated_at else model.created_at.strftime("%d/%m/%Y"),
                    description=model.description,
                    company_id=model.company_id,
                    features_inputs=None,
                    features_template=None,
                )
                for model in models
            ]

            return GetModelResponse(
                status=True,
                message='Modelos encontrados com sucesso.',
                data=models_data_list
            )

        except Exception as error:
            print(error)
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
        features_inputs: str,
        features_template: str,
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
            if features_inputs: model.features_inputs = features_inputs
            if features_template: model.features_template = features_template
            model.updated_at = datetime.utcnow() + timedelta(hours=-3)

            self._repository.update_model_repository(model, session)

            session.commit()

            return GetModelResponse(
                status=True,
                message='Dados do modelo atualizados.',
                data=GetModelData(
                    id=model.id,
                    name=model.name,
                    date=model.updated_at.strftime("%d/%m/%Y") if model.updated_at else model.created_at.strftime("%d/%m/%Y"),
                    description=model.description,
                    company_id=model.company_id,
                    features_inputs=model.features_inputs,
                    features_template=model.features_template,
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
                message='Modelo desativado com sucesso.',
                data=None
            )

        except Exception as error:
            session.rollback()
            return GetModelResponse(
                status=False,
                message='Erro interno no servidor.',
                data=None
            )
