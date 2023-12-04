from fastapi import HTTPException, status


class UserNotFoundError(HTTPException):
    def __init__(self, id: str | None = None, email: str | None = None) -> None:
        if id:
            detail = f"User with ID {id} not found."
        elif email:
            detail = f"User with email {email} not found."
        else:
            detail = "User not found."

        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class InvalidPasswordError(HTTPException):
    def __init__(self, email: str) -> None:
        detail = f"Password for user '{email}' does not match. Please check your credentials."
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)


class InternalServerError(HTTPException):
    def __init__(self, detail: str = "Internal Server Error.") -> None:
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)


class UserControllerException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class FileTypeNotSupportedError(HTTPException):
    def __init__(self, message: str):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)