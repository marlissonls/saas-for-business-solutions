# Definir middleware de autenticação
# Definir middleware de acesso ao bando de dados

from app.middlewares.database import db_session_middleware
from starlette.middleware.base import BaseHTTPMiddleware