from fastapi import Request, Response
from app.db import SessionLocal

class DBSessionMiddleware:
    def __init__(self, Session):
        self.Session = Session

    async def __call__(self, request: Request, call_next):
        response = Response("Internal server error", status_code=500)
        try:
            request.state.db = self.Session()
            response = await call_next(request)
        finally:
            request.state.db.close()
        return response

db_session_middleware = DBSessionMiddleware(SessionLocal)