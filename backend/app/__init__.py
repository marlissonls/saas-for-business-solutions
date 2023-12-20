from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from os.path import dirname
from fastapi.middleware.cors import CORSMiddleware
from app.middlewares import BaseHTTPMiddleware, db_session_middleware
from app.router import router

api = FastAPI()
    
api.mount(
    "/profile-photo",
    StaticFiles(directory=Path(f'{dirname(dirname(__file__))}\profile_images')),
    name="images",
)

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.add_middleware(
    BaseHTTPMiddleware,
    dispatch=db_session_middleware,
)

api.include_router(router)
