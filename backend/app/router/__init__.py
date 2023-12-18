from fastapi import APIRouter
from app.router import user_router
from app.router import mlmodel_router
from app.router import company_router

router = APIRouter()

router.include_router(user_router.router)
router.include_router(company_router.router)
router.include_router(mlmodel_router.router)