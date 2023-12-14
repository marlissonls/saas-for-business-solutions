from fastapi import APIRouter, Form, File, UploadFile, status, Depends, Request
from fastapi.responses import StreamingResponse
from app.repository.user.models.user_models import GetUserData, GetUserResponse, PutUser, LoginRequest, LoginResponse, RegisterResponse, GetProfileImage
from app.repository.user.sqlalchemy import UserRepository
from app.repository.user.controller import UserController
from app.repository.user.service import UserService
from app.utils.auth import get_authenticated_user
from typing import Any, Annotated
from sqlalchemy.orm import Session


repository = UserRepository()
service = UserService(repository)
controller = UserController(service)


router = APIRouter(prefix="/user", tags=["user"])


def get_db(request: Request):
    return request.state.db


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=GetUserResponse)
def get_user_by_id(user_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    if current_user['role'] == 'admin':
        return controller.get_user_by_id_controller(user_id, session)
    else:
        return GetUserResponse(
            status=False,
            message='Acesso negado.',
            data=None,
        )


@router.get('/profile-image/{user_id}', status_code=status.HTTP_200_OK, response_model=GetProfileImage)
def get_profile_image(user_id: str, current_user: dict = Depends(get_authenticated_user)):
    return controller.get_profile_image(user_id)


@router.get('/', status_code=status.HTTP_200_OK, response_model=GetUserResponse)
def get_users(current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    if current_user['role'] == 'admin':
        return controller.get_users_controller(session)
    else:
        return GetUserResponse(
            status=False,
            message='Acesso negado.',
            data=None,
        )


@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=RegisterResponse)
def create_user(
    name: Annotated[str, Form()],
    email: Annotated[str, Form()],
    password: Annotated[str, Form()],
    profile_image: Annotated[UploadFile, File()],
    session: Session = Depends(get_db)
) -> Any:
    return controller.create_user_controller(
        name,
        email,
        password,
        profile_image,
        session
    )


@router.post('/login', status_code=status.HTTP_201_CREATED, response_model=LoginResponse)
def login(form: LoginRequest, session: Session = Depends(get_db)) -> Any:
    return controller.login(form, session)


@router.put('/{user_id}', tags=['custom'], status_code=status.HTTP_200_OK, response_model=GetUserResponse)
def update_user(user_id: str, user: PutUser, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    return controller.update_user_controller(user_id, user, session)


@router.delete('/{user_id}', status_code=status.HTTP_200_OK, response_model=GetUserResponse)
def delete_user(user_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> None:
    controller.delete_user_controller(user_id, session)