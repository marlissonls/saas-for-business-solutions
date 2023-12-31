from fastapi import APIRouter, status, Request, Depends, Form
from app.repository.mlmodels.interfaces.model_interface import GetModelResponse, RegisterModelResponse, FeatureData, PredictResponse
from app.repository.mlmodels.sqlalchemy import ModelRepository
from app.repository.mlmodels.controller import ModelController
from app.repository.mlmodels.service import ModelService
from app.repository.mlmodels.predict_service import PredictService
from app.utils.auth import get_authenticated_user
from sqlalchemy.orm import Session
from typing import Any, Annotated, Optional

repository = ModelRepository()
service = ModelService(repository)
predict_service = PredictService()
controller = ModelController(service, predict_service)

router = APIRouter(prefix="/model", tags=["model"])

def get_db(request: Request):
    return request.state.db

@router.get('/{model_id}', status_code=status.HTTP_200_OK, response_model=GetModelResponse)
def get_model_by_id(model_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
        return controller.get_model_by_id_controller(model_id, session)

@router.get('/', status_code=status.HTTP_200_OK, response_model=GetModelResponse)
def get_models(company_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    return controller.get_models_controller(company_id, session)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=RegisterModelResponse)
def create_model(
    name: Annotated[str, Form()],
    description: Annotated[str, Form()],
    company_id: Annotated[str, Form()],
    current_user: dict = Depends(get_authenticated_user),
    session: Session = Depends(get_db)
) -> Any:
    return controller.create_model_controller(
        name,
        description,
        company_id,
        session
    )

@router.put('/{model_id}', status_code=status.HTTP_200_OK, response_model=GetModelResponse)
def update_model(
    model_id: str,
    name: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    features_inputs: Optional[str] = Form(None),
    features_template: Optional[str] = Form(None),
    jupyter_link: Optional[str] = Form(None),
    current_user: dict = Depends(get_authenticated_user),
    session: Session = Depends(get_db)
) -> Any:
    return controller.update_model_controller(
        model_id, 
        name,
        description,
        features_inputs,
        features_template,
        jupyter_link,
        session
        )

@router.delete('/{model_id}', status_code=status.HTTP_200_OK, response_model=GetModelResponse)
def delete_model(model_id: str, current_user: dict = Depends(get_authenticated_user), session: Session = Depends(get_db)) -> Any:
    if current_user['role'] == 'admin':
        return controller.delete_model_controller(model_id, session)
    else:
        return GetModelResponse(
            status=False,
            message='Acesso negado.',
            data=None,
        )


@router.post('/predict/{model_id}', status_code=status.HTTP_201_CREATED, response_model=PredictResponse)
def predict(model_id: str, features: FeatureData, current_user: dict = Depends(get_authenticated_user)) -> Any:
    return controller.predict_controller(model_id, features)