from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from app.router import router
from app.middlewares import BaseHTTPMiddleware, db_session_middleware
from os.path import dirname, exists

APP_SOURCE = f'{dirname(dirname(__file__))}'
PROFILE_IMAGES_PATH = f'{APP_SOURCE}\profile_images'
#STANDARD_PROFILE_IMAGE =  f'{APP_SOURCE}\standard_images'

profile_image_path = Path(PROFILE_IMAGES_PATH)

api = FastAPI()
    
api.mount("/profile-photo", StaticFiles(directory=profile_image_path), name="images")

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.add_middleware(BaseHTTPMiddleware, dispatch=db_session_middleware)

api.include_router(router)
