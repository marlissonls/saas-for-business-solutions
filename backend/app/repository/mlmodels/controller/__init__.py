from fastapi import Depends
from app.utils.auth import get_authenticated_user
from app.repository.mlmodels.models.model_models import PutModel, RegisterModelResponse, GetModelId, GetModelData, GetModelResponse
from app.repository.mlmodels.models.model_controller_interface import IModelController
from app.repository.mlmodels.models.model_service_interface import IModelService
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)

class ModelController(IModelController):

    def __init__(self, service: IModelService):
        self._service = service

    def get_model_by_id_controller(self, model_id: str, session: Session) -> GetModelResponse:
        try:
            return self._service.get_model_by_id_service(model_id, session)
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def get_models_controller(self, session: Session) -> GetModelResponse:
        try:
            return self._service.get_models_service(session)
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def create_model_controller(
        self,
        name: str,
        description: str,
        company_id: str ,
        session: Session
    ) -> RegisterModelResponse:
        try:
            return self._service.create_model_service(
                name,
                description,
                company_id,
                session
            )
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def update_model_controller(
        self, 
        model_id: str, 
        name: str,
        description: str,
        session: Session,
    ) -> GetModelResponse:
        try:
            return self._service.update_model_service(
                model_id, 
                name,
                description,
                session
                )
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def delete_model_controller(self, model_id: str, session: Session) -> GetModelResponse:
        try:
            self._service.delete_model_service(model_id, session)
        except Exception as error:
            logger.error("An error occurred: %s", error)
