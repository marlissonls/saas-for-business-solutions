from pydantic import BaseModel, EmailStr
from fastapi.responses import StreamingResponse
from typing import Optional, List, Union


class GetUserId(BaseModel):
    id: str

class PostUser(BaseModel):
    name: str
    email: EmailStr
    password: str

class GetUserData(BaseModel):
    id: str
    name: str
    email: EmailStr
    position: str | None
    company_id: str | None

class GetUserResponse(BaseModel):
    status: bool
    message: str
    data: Union[GetUserData, List[GetUserData], None] = None

class PutUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class RegisterResponse(BaseModel):
    status: bool
    message: str
    data: GetUserId | None

class CredentialInfo(BaseModel):
    token: str
    id: str
    username: str
    email: str
    position: str | None
    company_name: str | None
    role: str
    image_url: str | None

class LoginResponse(BaseModel):
    status: bool
    message: str 
    data: CredentialInfo | None

class LoginRequest(BaseModel):
    email: str
    password: str

class ImageUrl(BaseModel):
    image_url: str

class GetProfileImage(BaseModel):
    status: bool
    message: str
    data: ImageUrl