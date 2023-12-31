from app.repository.mlmodels.interfaces.model_repository_interface import IModelRepository
from app.db.schema import Model
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List


class ModelRepository(IModelRepository):

    def get_model_by_id_repository(self, model_id: str, session: Session) -> Model | None:
        return session.query(Model).filter(and_(Model.id == model_id, Model.deleted_at == None)).first()

    def get_models_repository(self, company_id: str, session: Session) -> List[Model] | List:
        return session.query(Model).filter(and_(Model.company_id == company_id, Model.deleted_at == None)).all()

    def create_model_repository(self, model: Model, session: Session) -> None:
        session.add(model)

    def update_model_repository(self, model: Model, session: Session) -> None:
        session.merge(model)

    def delete_model_repository(self, model: Model, session: Session) -> None:
        session.merge(model)


