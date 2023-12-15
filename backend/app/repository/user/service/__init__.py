from app.repository.user.models.user_models import GetUserId, GetUserData, GetUserResponse, LoginRequest, LoginResponse, CredentialInfo, RegisterResponse, GetProfileImage, ImageUrl
from app.repository.user.models.repository_interface import IUserRepository
from app.repository.user.models.service_interface import IUserService
from app.repository.user.service.handle_profile_image import FileTypeNotSupportedError, save_profile_photo, delete_profile_photo
from app.repository.user.service.hashing import Hasher
from app.db.schema import User
from app.config import jwt_configs
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import Column
from fastapi import UploadFile
from uuid import uuid1
import jwt


class UserService(IUserService):

    def __init__(self, repository: IUserRepository):
        self._repository = repository

    def get_user_by_id_service(self, user_id: str, session: Session) -> GetUserResponse:
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


    def get_profile_image(self, user_id: str) -> GetProfileImage:
        return GetProfileImage(
            status=True,
            message='OK',
            data=ImageUrl(
                image_url=f"/profile-photo/{user_id}.jpeg"
            )
        )


    def get_users_service(self, session: Session) -> GetUserResponse:
        try:
            users = self._repository.get_users_repository(session)

            if not users:
                return GetUserResponse(
                    status=True,
                    message='Nenhum usuário encontrado nesta pesquisa.',
                    data=[]
                )
            
            users_data_list = [GetUserData(id=user.id, name=user.name, email=user.email, company_id=user.company_id) for user in users]
            return GetUserResponse(
                status=True,
                message='Usuários encontrados com sucesso.',
                data=users_data_list
            )

        except Exception as error:
            session.rollback()
            return GetUserResponse(
                status=False,
                message='Erro interno no servidor.',
                data=None
            )


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

            profile_photo_name = f'{new_user_id}.jpeg'
            profile_photo_url = f'/profile-photo/{profile_photo_name}'

            new_user = User(
                id=new_user_id,
                name=name,
                email=email,
                password=Hasher.get_password_hash(password),
                profile_image=profile_photo_url,
                role='client'
            )

            self._repository.create_user_repository(new_user, session)

            save_profile_photo(profile_photo_name, profile_image)

            session.commit()

            return RegisterResponse(
                status=True,
                message=f"Usuário {name} cadastrado com sucesso.",
                data=GetUserId(id=new_user.id)
            )

        except FileTypeNotSupportedError:
            session.rollback()
            return RegisterResponse(
                status=False,
                message=f"Arquivo não suportado.",
                data=None
            )
        except Exception as error:
            session.rollback()
            return RegisterResponse(
                status=False,
                message=f"Erro ao cadastrar este usuário.",
                data=None
            )


    def login(self, form: LoginRequest, session: Session) -> LoginResponse:
        try:
            user = self._repository.get_user_by_email_repository(form.email, session)

            if not user:
                return LoginResponse(
                    status=False,
                    message="Falha ao realizar login, verifique suas credenciais.",
                    data=None
                )
            
            user_company: Column[str] | None = None
            
            if user.company_id:
                user_company = self._repository.get_user_company_name(user.company_id, session)

            if not Hasher.verify_password(form.password, user.password):
                return LoginResponse(
                    status=False,
                    message="Senha inválida.",
                    data=None
                )

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
                    position=user.position,
                    company_name=user_company,
                    role=user.role,
                    image_url=user.profile_image
                )
            )

        except Exception as error:
            session.rollback()
            return LoginResponse(
                    status=False,
                    message="Erro interno no servidor.",
                    data=None
                )


    def update_user_service(
        self,
        user_id: str,
        name: str,
        email: str,
        position: str,
        password: str,
        profile_image: UploadFile,
        session: Session
    ) -> GetUserResponse:
        try:
            user = self._repository.get_user_by_id_repository(user_id, session)

            if not user:
                return GetUserResponse(
                    status=False,
                    message='Não foi possível encontrar este usuário.',
                    data=None
                )

            if name: user.name = name
            if email: user.email = email
            if position: user.position = position
            if password: user.password = Hasher.get_password_hash(password)
            user.updated_at = datetime.utcnow() + timedelta(hours=-3)

            self._repository.update_user_repository(user, session)

            if profile_image:
                profile_photo_name = f'{user_id}.jpeg'
                save_profile_photo(profile_photo_name, profile_image)

            session.commit()

            return GetUserResponse(
                status=True,
                message='Dados atualizados.',
                data=GetUserData(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    position=user.position,
                    company_id=user.company_id
                )
            )
        except Exception as error:
            session.rollback()
            return GetUserResponse(
                status=False,
                message='Erro interno no servidor.',
                data=None
            )


    def delete_user_service(self, user_id: str, session: Session) -> GetUserResponse:
        try:
            user = self._repository.get_user_by_id_repository(user_id, session)

            if not user:
                return GetUserResponse(
                    status=False,
                    message='Não foi possível encontrar este usuário.',
                    data=None
                )
            
            user.deleted_at = datetime.utcnow()+timedelta(hours=-3)

            self._repository.delete_user_repository(user, session)

            delete_profile_photo(user_id)

            session.commit()

            return GetUserResponse(
                status=True,
                message='Usuário deletado.',
                data=None
            )

        except Exception as error:
            session.rollback()
            return GetUserResponse(
                status=False,
                message='Erro interno no servidor.',
                data=None
            )