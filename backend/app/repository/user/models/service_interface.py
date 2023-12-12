from app.repository.user.models.user_models import GetUserResponse, PutUser, LoginRequest, LoginResponse, RegisterResponse, GetProfileImage
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from fastapi import UploadFile

class IUserService(ABC):

    @abstractmethod
    def get_user_by_id_service(self, user_id: str, session: Session) -> GetUserResponse:
        pass

    @abstractmethod
    def get_profile_image(self, user_id: str) -> GetProfileImage:
        pass

    @abstractmethod
    def get_users_service(self, session: Session) -> GetUserResponse:
        pass

    @abstractmethod
    def create_user_service(
        self, 
        name: str,
        email: str,
        password: str,
        profile_image: UploadFile,
        session: Session
    ) -> RegisterResponse:
        pass

    @abstractmethod
    def login(self, form: LoginRequest, session: Session) -> LoginResponse:
        pass

    @abstractmethod
    def update_user_service(self, user_id: str, user_updated: PutUser, session: Session) -> GetUserResponse:
        pass

    @abstractmethod
    def delete_user_service(self, user_id: str, session: Session) -> GetUserResponse:
        pass