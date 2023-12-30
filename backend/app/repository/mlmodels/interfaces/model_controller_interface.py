from app.repository.mlmodels.interfaces.model_interface import GetModelResponse, RegisterModelResponse, PutModel
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod

class IModelController(ABC):

    @abstractmethod
    def get_model_by_id_controller(self, model_id: str, session: Session) -> GetModelResponse:
        pass
    
    @abstractmethod
    def get_models_controller(self, session: Session) -> GetModelResponse:
        pass

    @abstractmethod
    def create_model_controller(
        self, 
        name: str,
        description: str,
        session: Session
    ) -> RegisterModelResponse:
        pass

    @abstractmethod
    def update_model_controller(self, model_id: str, model: PutModel, session: Session) -> GetModelResponse:
        pass

    @abstractmethod
    def delete_model_controller(self, model_id: str, session: Session) -> GetModelResponse:
        pass
