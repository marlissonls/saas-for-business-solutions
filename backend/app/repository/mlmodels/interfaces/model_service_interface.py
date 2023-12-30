from app.repository.mlmodels.interfaces.model_interface import PutModel, GetModelResponse, RegisterModelResponse
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import List

class IModelService(ABC):

    @abstractmethod
    def get_model_by_id_service(self, model_id: str) -> GetModelResponse:
        pass

    @abstractmethod
    def get_models_service(self) -> GetModelResponse:
        pass

    @abstractmethod
    def create_model_service(
        self, 
        name: str,
        description: str,
        session: Session
    ) -> RegisterModelResponse:
        pass

    @abstractmethod
    def update_model_service(self, model_id: str, model_updated: PutModel) -> GetModelResponse:
        pass

    @abstractmethod
    def delete_model_service(self, model_id: str) -> None:
        pass
