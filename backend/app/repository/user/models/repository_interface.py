from app.db.schema import User
from sqlalchemy import Column
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod


class IUserRepository(ABC):

    @abstractmethod
    def get_user_by_id_repository(self, user_id: str, session: Session) -> User | None:
        pass

    @abstractmethod
    def get_users_repository(self, session: Session) -> list[User] | list:
        pass
    
    @abstractmethod
    def get_user_by_email_repository(self, email: str, session: Session) -> User | None:
        pass
    
    @abstractmethod
    def get_user_company_name(self, company_id: str, session: Session) -> Column[str] | None:
        pass

    @abstractmethod
    def create_user_repository(self, user: User, session: Session) -> None:
        pass

    @abstractmethod
    def update_user_repository(self, user: User, session: Session) -> None:
        pass

    @abstractmethod
    def delete_user_repository(self, user: User, session: Session) -> None:
        pass