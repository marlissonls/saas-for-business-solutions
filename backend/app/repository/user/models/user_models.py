from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class GetUserId(BaseModel):
    id: str

class PostUser(UserBase):
    password: str

class GetUser(GetUserId, UserBase):
    pass

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

class LoginResponse(BaseModel):
    status: bool
    message: str 
    data: CredentialInfo | None

class LoginRequest(BaseModel):
    email: str
    password: str