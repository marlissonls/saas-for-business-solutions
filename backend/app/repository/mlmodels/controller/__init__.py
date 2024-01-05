from app.repository.mlmodels.interfaces.model_interface import RegisterModelResponse, GetModelResponse, FeatureData, PredictResponse
from app.repository.mlmodels.interfaces.model_controller_interface import IModelController
from app.repository.mlmodels.interfaces.model_service_interface import IModelService
from app.repository.mlmodels.interfaces.model_predict_service_interface import IPredictService
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger(__name__)

class ModelController(IModelController):

    def __init__(self, service: IModelService, predict_service: IPredictService):
        self._service = service
        self._predict = predict_service

    def get_model_by_id_controller(self, model_id: str, session: Session) -> GetModelResponse:
        try:
            return self._service.get_model_by_id_service(model_id, session)
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def get_models_controller(self, company_id: str, session: Session) -> GetModelResponse:
        try:
            return self._service.get_models_service(company_id, session)
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
        features_inputs: str,
        features_template: str,
        jupyter_link: str,
        session: Session,
    ) -> GetModelResponse:
        try:
            return self._service.update_model_service(
                model_id, 
                name,
                description,
                features_inputs,
                features_template,
                jupyter_link,
                session
            )
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def delete_model_controller(self, model_id: str, session: Session) -> GetModelResponse:
        try:
            return self._service.delete_model_service(model_id, session)
        except Exception as error:
            logger.error("An error occurred: %s", error)

    def predict_controller(self, model_id: str, features: FeatureData) -> PredictResponse:
        try:
            return self._predict.predict_service(model_id, features)
        except Exception as error:
            logger.error("An error occurred: %s", error)