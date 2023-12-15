from app.repository.user.models.user_models import GetUserResponse, LoginRequest, LoginResponse, RegisterResponse, GetProfileImage
from app.repository.user.models.controller_interface import IUserController
from app.repository.user.models.service_interface import IUserService
from sqlalchemy.orm import Session
from fastapi import UploadFile
import logging

logger = logging.getLogger(__name__)


class UserController(IUserController):

    def __init__(self, service: IUserService):
        self._service = service

    def get_user_by_id_controller(self, user_id: str, session: Session) -> GetUserResponse:
        try:
            return self._service.get_user_by_id_service(user_id, session)
        except Exception as error:
            logger.error("An error occurred: %s", error)
    

    def get_profile_image(self, user_id: str) -> GetProfileImage:
        try:
            return self._service.get_profile_image(user_id)
        except Exception as error:
            logger.error("An error occurred: %s", error)


    def get_users_controller(self, session: Session) -> GetUserResponse:
        try:
            return self._service.get_users_service(session)
        except Exception as error:
            logger.error("An error occurred: %s", error)


    def create_user_controller(
        self, 
        name: str,
        email: str,
        password: str,
        profile_image: UploadFile,
        session: Session
    ) -> RegisterResponse:
        try:
            return self._service.create_user_service(
                name,
                email,
                password,
                profile_image,
                session
            )
        except Exception as error:
            logger.error("An error occurred: %s", error)


    def login(self, form: LoginRequest, session: Session) -> LoginResponse:
        try:
            return self._service.login(form, session)
        except Exception as error:
            logger.error("An error occurred: %s", error)


    def update_user_controller(
        self,
        user_id: str,
        name: str,
        email: str,
        password: str,
        profile_image: UploadFile,
        session: Session
    ) -> GetUserResponse:
        try:
            return self._service.update_user_service(
                user_id,
                name,
                email,
                password,
                profile_image,
                session
            )
        except Exception as error:
            logger.error("An error occurred: %s", error)


    def delete_user_controller(self, user_id: str, session: Session) -> GetUserResponse:
        try:
            self._service.delete_user_service(user_id, session)
        except Exception as error:
            logger.error("An error occurred: %s", error)
