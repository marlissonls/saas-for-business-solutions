from app.repository.user.models.repository_interface import IUserRepository
from app.db.schema import UserSchema
from sqlalchemy.orm import Session
from typing import List


class UserRepository(IUserRepository):

    def get_user_by_id_repository(self, user_id: str, session: Session) -> UserSchema | None:
        return session.query(UserSchema).filter(UserSchema.id == user_id).first()


    def get_users_repository(self, session: Session) -> List[UserSchema]:
        return session.query(UserSchema).all()
    

    def get_user_by_email_repository(self, email: str, session: Session) -> UserSchema | None:
        return  session.query(UserSchema).filter(UserSchema.email == email).first()
        

    def create_user_repository(self, user: UserSchema, session: Session) -> None:
        session.add(user)


    def update_user_repository(self, user: UserSchema, session: Session) -> None:
        session.merge(user)


    def delete_user_repository(self, user: UserSchema, session: Session) -> None:
        session.delete(user)