from fastapi import FastAPI
from app.router import router
from app.middlewares import BaseHTTPMiddleware, db_session_middleware

api = FastAPI()

api.add_middleware(BaseHTTPMiddleware, dispatch=db_session_middleware)

api.include_router(router)