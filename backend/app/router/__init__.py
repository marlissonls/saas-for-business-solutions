# post cadastro user
# post login user
# update user
# deletar user
# 
# pegar dash
# criar dash
# editar dash
# deletar dash
# 
# pegar modelo
# criar modelo
# editar modelo
# deletar modelo

from fastapi import APIRouter, status, Header
from fastapi.exceptions import HTTPException
import jwt

from app.router import user_routes
from app.config import jwt_configs

router = APIRouter()

router.include_router(user_routes.router)

@router.get('/', status_code=status.HTTP_200_OK)
def root(authorization_token: str | None = Header(default=None)):
    return checkToken(authorization_token)

def checkToken (token: str):
    token_bytes = token.encode('utf-8')
    payload = jwt.decode(token_bytes, jwt_configs["hash_key"], algorithms=["HS256"], verify=True)
    if payload:
        return payload
    return HTTPException(status.HTTP_401_UNAUTHORIZED, "Token is unauthorized")
