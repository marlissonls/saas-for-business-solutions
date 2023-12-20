from pydantic import BaseModel
from typing import Optional, List, Union

class GetDashboardId(BaseModel):
    id: str

class PostDashboard(BaseModel):
    name: str
    description: str

class GetDashboardData(BaseModel):
    id: str
    name: str
    date: str
    description: str
    company_id: str

class GetDashboardResponse(BaseModel):
    status: bool
    message: str
    data: Union[GetDashboardData, List[GetDashboardData], None] = None

class PutDashboard(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class RegisterDashboardResponse(BaseModel):
    status: bool
    message: str
    data: GetDashboardId | None
