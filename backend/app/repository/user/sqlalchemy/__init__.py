from app.repository.user.models.repository_interface import IUserRepository
from app.db.schema import User, Company
from sqlalchemy.orm import Session
from sqlalchemy import and_, Column
from typing import List


class UserRepository(IUserRepository):

    def get_user_by_id_repository(self, user_id: str, session: Session) -> User | None:
        return session.query(User).filter(and_(User.id == user_id, User.deleted_at == None)).first()


    def get_users_repository(self, session: Session) -> List[User] | List:
        return session.query(User).filter(User.deleted_at == None).all()


    def get_user_by_email_repository(self, email: str, session: Session) -> User | None:
        return session.query(User).filter(and_(User.email == email, User.deleted_at == None)).first()


    def get_user_company_name(self, company_id: str, session: Session) -> Column[str] | None:
        return session.query(Company).filter(Company.id == company_id).first().name


    def create_user_repository(self, user: User, session: Session) -> None:
        session.add(user)


    def update_user_repository(self, user: User, session: Session) -> None:
        session.merge(user)


    def delete_user_repository(self, user: User, session: Session) -> None:
        session.merge(user)