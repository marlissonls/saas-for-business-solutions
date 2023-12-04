from pydantic import BaseModel, EmailStr

class HomePage(BaseModel):
    get_users: str

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserId(BaseModel):
    id: str

class UserIn(UserBase):
    password: str

class UserOut(UserId, UserBase):
    pass

class ResLogin(UserId, UserBase):
    token: str

class UserForm(BaseModel):
    email: str
    password: str