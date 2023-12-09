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

class CredentialInfo(BaseModel):
    token: str
    username: str

class LoginResponse(BaseModel):
    status: bool
    message: str 
    data: CredentialInfo

class LoginRequest(BaseModel):
    email: str
    password: str