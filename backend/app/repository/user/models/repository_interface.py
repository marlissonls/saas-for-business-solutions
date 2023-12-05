from app.db.schema import User
from app.repository.user.models.user_models import UserIn
from sqlalchemy.orm import Session as SQLAlchemySession
from abc import ABC, abstractmethod
from typing import Any, List

# repository.user.models.user_models

class IUserRepository(ABC):

    @abstractmethod
    def get_user_by_id_repository(self, client: SQLAlchemySession, user_id: str) -> User | None:
        pass

    @abstractmethod
    def get_users_repository(self, client: SQLAlchemySession) -> List[User]:
        pass
    
    @abstractmethod
    def get_user_by_email_repository(self, client: SQLAlchemySession, name: str) -> User | None:
        pass

    @abstractmethod
    def create_user_repository(self, client: SQLAlchemySession, user: UserIn) -> None:
        pass

    @abstractmethod
    def update_user_repository(self, client: SQLAlchemySession, user: User) -> None:
        pass

    @abstractmethod
    def delete_user_repository(self, client: SQLAlchemySession, user: User) -> None:
        pass