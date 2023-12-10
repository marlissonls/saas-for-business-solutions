from app.repository.user.models.user_models import PostUser, GetUser, GetUserId, LoginRequest, LoginResponse
from abc import ABC, abstractmethod

class IUserController(ABC):

    @abstractmethod
    def get_user_by_id_controller(self, user_id: str) -> GetUser:
        pass

    @abstractmethod
    def get_users_controller(self) -> list[GetUser]:
        pass

    @abstractmethod
    def create_user_controller(self, user: PostUser) -> GetUserId:
        pass
    
    @abstractmethod
    def login(self, form: LoginRequest) -> LoginResponse:
        pass

    @abstractmethod
    def update_user_controller(self, user_id: str, user: PostUser) -> GetUser:
        pass

    @abstractmethod
    def delete_user_controller(self, user_id: str) -> None:
        pass