from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import router
from app.middlewares import BaseHTTPMiddleware, db_session_middleware

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.add_middleware(BaseHTTPMiddleware, dispatch=db_session_middleware)

api.include_router(router)
