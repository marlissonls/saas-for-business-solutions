from fastapi import APIRouter, Form, File, UploadFile, status, Depends, Request
from app.repository.user.models.user_models import UserIn, UserOut, UserId, UserForm, ResLogin
from app.repository.user.sqlalchemy import UserRepository
from app.repository.user.controller import UserController
from app.repository.user.service import UserService
from typing import Any, Annotated
from sqlalchemy.orm import Session


repository = UserRepository()
service = UserService(repository)
controller = UserController(service)


router = APIRouter(prefix="/user", tags=["user"])


def get_db(request: Request):
    return request.state.db


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=UserOut)
def get_user_by_id(user_id: str, session: Session = Depends(get_db)) -> Any:
    return controller.get_user_by_id_controller(user_id, session)


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[UserOut])
def get_users(session: Session = Depends(get_db)) -> Any:
    return controller.get_users_controller(session)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserId)
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


@router.post('/checkuser', status_code=status.HTTP_200_OK, response_model=ResLogin)
def check_user(form: UserForm, session: Session = Depends(get_db)) -> Any:
    return controller.check_user_controller(form, session)


@router.put('/{user_id}', tags=['custom'], status_code=status.HTTP_200_OK, response_model=UserOut)
def update_user(user_id: str, user: UserIn, session: Session = Depends(get_db)) -> Any:
    return controller.update_user_controller(user_id, user, session)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, session: Session = Depends(get_db)) -> None:
    controller.delete_user_controller(user_id, session)