from app.db.schema import Model
from app.repository.mlmodels.models.model_models import PutModel
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from typing import List


class IModelRepository(ABC):

    @abstractmethod
    def get_model_by_id_repository(self, model_id: str, session: Session) -> Model | None:
        pass

    @abstractmethod
    def get_models_repository(self, session: Session) -> List[Model] | List:
        pass
    
    @abstractmethod
    def create_model_repository(self, model: Model, session: Session) -> None:
        pass

    @abstractmethod
    def update_model_repository(self, model: Model, session: Session) -> None:
        pass

    @abstractmethod
    def delete_model_repository(self, model: Model, session: Session) -> None:
        pass
