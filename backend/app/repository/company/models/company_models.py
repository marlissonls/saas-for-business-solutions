from pydantic import BaseModel, EmailStr
from typing import Optional, List, Union

class GetCompanyId(BaseModel):
    id: str

class PostCompany(BaseModel):
    name: str
    area: str
    description: str
    localization: str

class GetCompanyData(BaseModel):
    id: str
    name: str
    area: str
    description: str
    localization: str

class GetCompanyResponse(BaseModel):
    status: bool
    message: str
    data: Union[GetCompanyData, List[GetCompanyData], None] = None

class PutCompany(BaseModel):
    name: Optional[str] = None
    area: Optional[str] = None
    description: Optional[str] = None
    localization: Optional[str] = None

class RegisterCompanyResponse(BaseModel):
    status: bool
    message: str
    data: GetCompanyId | None
