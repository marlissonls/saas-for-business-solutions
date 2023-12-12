from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt

from app.config import jwt_configs

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = jwt_configs["hash_key"]
ALGORITHM = jwt_configs["algorithm"]

def handle_token_exception(exception: Exception) -> None:
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=str(exception),
        headers={"WWW-Authenticate": "Bearer"},
    )

async def get_authenticated_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user: dict = payload.get("sub")
        if user is None:
            handle_token_exception(HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Não foi possível validar as credenciais. Verifique o token ou faça login novamente.",
                headers={"WWW-Authenticate": "Bearer"},
            ))
    except jwt.ExpiredSignatureError as e:
        handle_token_exception(e)
    except jwt.InvalidTokenError as e:
        handle_token_exception(e)

    return user

