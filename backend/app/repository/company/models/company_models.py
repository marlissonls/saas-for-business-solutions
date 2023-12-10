from pydantic import BaseModel

class CompanyBase(BaseModel):
    name: str
    description : str

class CompanyId(BaseModel):
    id: str

class CompanyIn(CompanyBase):
    pass

class CompanyOut(CompanyId, CompanyBase):
    pass

class Data(BaseModel):
    token: str
    company_name: str

class ResLogin(BaseModel):
    status: bool
    message: str 
    data: Data

class CompanyForm(BaseModel):
    name: str
    description : str
