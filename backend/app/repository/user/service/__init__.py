from app.repository.user.exceptions import UserNotFoundError, InternalServerError, FileTypeNotSupportedError
from app.repository.user.models.user_models import PutUser, GetUserId, GetUserData, GetUserResponse, LoginRequest, LoginResponse, CredentialInfo, RegisterResponse
from app.repository.user.models.repository_interface import IUserRepository
from app.repository.user.models.service_interface import IUserService
from app.repository.user.service.handle_profile_image import save_profile_image, get_profile_image
from app.repository.user.service.hashing import Hasher
from app.db.schema import User
from app.config import jwt_configs

from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import UploadFile
from uuid import uuid1
import jwt


class UserService(IUserService):

    def __init__(self, repository: IUserRepository):
        self._repository = repository

    def get_user_by_id_service(self, user_id: str, session: Session) -> GetUserData:
        error = None
        try:
            user = self._repository.get_user_by_id_repository(user_id, session)

            if not user:
                return GetUserResponse(
                    status=False,
                    message='Não foi possível encontrar este usuário.',
                    data=None
                )
            
            return GetUserResponse(
                status=True,
                message='Usuário encontrado com sucesso.',
                data=GetUserData(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    company_id=user.company_id
                )
            )

        except Exception as error:
            session.rollback()
            return GetUserResponse(
                status=False,
                message=f'Erro interno no servidor',
                data=None
            )
        finally:
            if error:
                raise error


    def get_users_service(self, session: Session) -> list[GetUserData] | list:
        try:
            users = self._repository.get_users_repository(session)

            if not users:
                return []
            
            return [GetUserData(id=user.id, name=user.name, email=user.email) for user in users]

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
    ) -> RegisterResponse:
        try:
            new_user_id = str(uuid1())

            profile_image_name = f'{new_user_id}.jpeg'

            new_user = User(
                id=new_user_id,
                name=name,
                email=email,
                password=Hasher.get_password_hash(password),
                profile_image=profile_image_name,
                role='client'
            )

            self._repository.create_user_repository(new_user, session)

            save_profile_image(profile_image_name, profile_image)

            session.commit()

            return RegisterResponse(
                status=True,
                message=f"Usuário {name} cadastrado com sucesso.",
                data=GetUserId(id=new_user.id)
            )

        except SQLAlchemyError as error:
            session.rollback()
            return RegisterResponse(
                status=False,
                message=f"Erro ao cadastrar este usuário.",
                data=None
            )
        except FileTypeNotSupportedError as error:
            session.rollback()
            raise


    def login(self, form: LoginRequest, session: Session) -> LoginResponse:
        try:
            user = self._repository.get_user_by_email_repository(form.email, session)

            if not user:
                return LoginResponse(
                    status=False,
                    message="Falha ao realizar login, verifique suas credenciais.",
                    data=None
                )

            if Hasher.verify_password(form.password, user.password):
                return LoginResponse(
                    status=True,
                    message="Login realizado com sucesso",
                    data=CredentialInfo(
                        token=jwt.encode(
                            {"sub": {"id": user.id, "name": user.name, "email": user.email, "role": user.role},
                             "exp": datetime.utcnow() + timedelta(days=10)},
                            jwt_configs["hash_key"],
                            algorithm=jwt_configs['algorithm']
                        ),
                        id=user.id,
                        username=user.name,
                        email=user.email,
                        role=user.role,
                        profile=get_profile_image(user.id)
                    )
                )

            else:
                return LoginResponse(
                    status=False,
                    message="Senha inválida.",
                    data=None
                )
        except SQLAlchemyError as error:
            session.rollback()
            return LoginResponse(
                    status=False,
                    message="Erro interno no servidor.",
                    data=None
                )


    def update_user_service(self, user_id: str, user_updated: PutUser, session: Session) -> GetUserData:
        try:
            user = self._repository.get_user_by_id_repository(user_id, session)

            if not user:
                raise UserNotFoundError(id=user_id)
            
            for key, value in user_updated.model_dump(exclude_unset=True).items():
                if key == 'password' and value is not None:
                    setattr(user, key, Hasher.get_password_hash(value))
                else:
                    setattr(user, key, value)

            user.updated_at = datetime.utcnow()+timedelta(hours=-3)

            self._repository.update_user_repository(user, session)

            session.commit()

            return GetUserData(
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
            
            user.deleted_at = datetime.utcnow()+timedelta(hours=-3)

            self._repository.delete_user_repository(user, session)

            session.commit()

        except SQLAlchemyError as error:
            session.rollback()
            raise InternalServerError(f"SQLAlchemyError: {str(error)}") from error