from app.repository.user.exceptions import UserNotFoundError, InvalidPasswordError, UserControllerException, FileTypeNotSupportedError
from app.repository.user.models.user_models import GetUserId, GetUser, PostUser, LoginRequest, LoginResponse
from app.repository.user.models.controller_interface import IUserController
from app.repository.user.models.service_interface import IUserService
from sqlalchemy.orm import Session
from fastapi import UploadFile
import logging

logger = logging.getLogger(__name__)


class UserController(IUserController):

    def __init__(self, service: IUserService):
        self._service = service

    def get_user_by_id_controller(self, user_id: str, session: Session) -> GetUser:
        try:
            return self._service.get_user_by_id_service(user_id, session)
        except UserNotFoundError as error:
            logger.error("User not found: %s", error)
            raise
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to fetch user by ID.") from error


    def get_users_controller(self, session: Session) -> list[GetUser] | list:
        try:
            return self._service.get_users_service(session)
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to fetch users.") from error


    def create_user_controller(
        self, 
        name: str,
        email: str,
        password: str,
        profile_image: UploadFile,
        session: Session
    ) -> GetUserId:
        try:
            return self._service.create_user_service(
                name,
                email,
                password,
                profile_image,
                session
            )
        except FileTypeNotSupportedError as error:
            logger.error("Profile image must be an image: %s", error)
            raise
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to create user.") from error


    def login(self, form: LoginRequest, session: Session) -> LoginResponse:
        try:
            return self._service.login(form, session)
        except UserNotFoundError as error:
            logger.error("User not found: %s", error)
            raise
        except InvalidPasswordError as error:
            logger.error("Invalid password: %s", error)
            raise
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to fetch user by email.") from error


    def update_user_controller(self, user_id: str, user: PostUser, session: Session) -> GetUser:
        try:
            return self._service.update_user_service(user_id, user, session)
        except UserNotFoundError as error:
            logger.error("User not found: %s", error)
            raise
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to update user.") from error


    def delete_user_controller(self, user_id: str, session: Session) -> None:
        try:
            self._service.delete_user_service(user_id, session)
        except UserNotFoundError as error:
            logger.error("User not found: %s", error)
            raise
        except Exception as error:
            logger.error("An error occurred: %s", error)
            raise UserControllerException("Failed to delete user.") from error
