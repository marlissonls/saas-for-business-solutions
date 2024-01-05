from pydantic import BaseModel
from typing import Optional, List, Union

class GetModelId(BaseModel):
    id: str

class PostModel(BaseModel):
    name: str
    description: str

class GetModelData(BaseModel):
    id: str
    name: str
    date: str
    description: str
    company_id: str
    features_inputs: Union[str, None]
    features_template: Union[str, None]
    jupyter_link: Union[str, None]

class GetModelResponse(BaseModel):
    status: bool
    message: str
    data: Union[GetModelData, List[GetModelData], None] = None

class PutModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class RegisterModelResponse(BaseModel):
    status: bool
    message: str
    data: GetModelId | None

class FeatureData(BaseModel):
    features_values: dict
    features_template: dict

class PredictResponse(BaseModel):
    status: bool
    message: str
    data: Union[List, int, str, bool, None] = None