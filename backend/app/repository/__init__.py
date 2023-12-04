# Realizar a comunicação com o banco de dados.
# Utilização do framework sqlAlchemy.
from app.repository.user.exceptions import UserNotFoundError, InvalidPasswordError, InternalServerError, FileTypeNotSupportedError
from app.repository.user.models.user_models import UserIn, UserOut, UserId, UserForm
from app.repository.user.models.repository_interface import IUserRepository
from app.repository.user.models.service_interface import IUserService
from app.repository.user.service.save_profile_image import save_profile_image
from app.repository.user.service.hashing import Hasher
from app.db.schema import UserSchema
from app import config
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import UploadFile
from uuid import uuid1
import jwt


class UserService(IUserService):

    def __init__(self, repository: IUserRepository):
        self._repository = repository

    def get_user_by_id_service(self, user_id: str, session: Session) -> UserOut:
        try:
            user = self._repository.get_user_by_id_repository(session, user_id)

            if not user:
                raise UserNotFoundError(id=user_id)
            
            return UserOut(
                id=user.id,
                name=user.name,
                email=user.email
            )

        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except Exception as error:
            raise InternalServerError(f"Internal Server Error: {str(error)}") from error


    def get_users_service(self, session: Session) -> list[UserOut] | list:
        try:
            users = self._repository.get_users_repository(session)

            if not users:
                return []
            
            return [UserOut(id=user.id, name=user.name, email=user.email) for user in users]

        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except Exception as error:
            raise InternalServerError(f"Internal Server Error: {str(error)}") from error


    def create_user_service(
        self, 
        name: str,
        email: str,
        password: str,
        profile_image: UploadFile,
        session: Session
    ) -> UserId:
        try:
            new_user_id = str(uuid1())

            profile_image_name = f'{new_user_id}.jpeg'

            new_user = UserSchema(
                id=new_user_id,
                name=name,
                email=email,
                password=Hasher.get_password_hash(password),
                profile_image=profile_image_name
            )

            self._repository.create_user_repository(new_user, session)

            save_profile_image(profile_image_name, profile_image)

            session.commit()

            return UserId(id=new_user.id)

        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error
        except FileTypeNotSupportedError as error:
            session.rollback()
            raise


    def check_user_service(self, form: UserForm, session: Session) -> UserOut:
        try:
            user = self._repository.get_user_by_name_repository(form.email, session)

            if not user:
                raise UserNotFoundError(email=form.email)

            if Hasher.verify_password(form.password, user.password):
                return UserOut(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    token=jwt.encode(
                        {"email": user.email, "type": "admin"},
                        configs.jwt_configs["hash_key"],
                        algorithm="HS256"
                    )
                )
            else:
                raise InvalidPasswordError(email=form.email)
        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error


    def update_user_service(self, user_id: str, user_updated: UserIn, session: Session) -> UserOut:
        try:
            user = self._repository.get_user_by_id_repository(user_id, session)

            if not user:
                raise UserNotFoundError(id=user_id)

            user.name = user_updated.name
            user.email = user_updated.email
            user.password = Hasher.get_password_hash(user_updated.password)

            self._repository.update_user_repository(user, session)

            session.commit()

            return UserOut(
                id=user.id,
                name=user.name,
                email=user.email
            )
        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error


    def delete_user_service(self, user_id: str, session: Session) -> None:
        try:
            user = self._repository.get_user_by_id_repository(user_id, session)

            if not user:
                raise UserNotFoundError(id=user_id)

            self._repository.delete_user_repository(user, session)

            session.commit()

        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error