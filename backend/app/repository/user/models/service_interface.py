from app.repository.user.models.user_models import GetUserId, GetUserData, PostUser, LoginRequest
from abc import ABC, abstractmethod

class IUserService(ABC):

    @abstractmethod
    def get_user_by_id_service(self, user_id: str) -> GetUserData:
        pass

    @abstractmethod
    def get_users_service(self) -> list[GetUserData]:
        pass

    @abstractmethod
    def create_user_service(self, user: PostUser) -> GetUserId:
        pass

    @abstractmethod
    def login(self, form: LoginRequest) -> GetUserData:
        pass

    @abstractmethod
    def update_user_service(self, user_id: str, user_updated: PostUser) -> GetUserData:
        pass

    @abstractmethod
    def delete_user_service(self, user_id: str) -> None:
        pass