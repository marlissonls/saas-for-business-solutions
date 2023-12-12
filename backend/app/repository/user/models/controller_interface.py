from app.repository.user.models.user_models import GetUserResponse, PutUser, LoginRequest, LoginResponse, RegisterResponse, GetProfileImage
from sqlalchemy.orm import Session
from fastapi import UploadFile
from abc import ABC, abstractmethod

class IUserController(ABC):

    @abstractmethod
    def get_user_by_id_controller(self, user_id: str, session: Session) -> GetUserResponse:
        pass
    
    @abstractmethod
    def get_profile_image(self, user_id: str) -> GetProfileImage:
        pass

    @abstractmethod
    def get_users_controller(self, session: Session) -> GetUserResponse:
        pass

    @abstractmethod
    def create_user_controller(
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
    def update_user_controller(self, user_id: str, user: PutUser, session: Session) -> GetUserResponse:
        pass

    @abstractmethod
    def delete_user_controller(self, user_id: str, session: Session) -> GetUserResponse:
        pass