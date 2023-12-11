from pydantic import BaseModel, EmailStr
from typing import Optional


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
    company_id: str | None

class GetUserResponse(BaseModel):
    status: bool
    message: str
    data: GetUserData | None

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
    role: str
    profile: bytes

class LoginResponse(BaseModel):
    status: bool
    message: str 
    data: CredentialInfo | None

class LoginRequest(BaseModel):
    email: str
    password: str