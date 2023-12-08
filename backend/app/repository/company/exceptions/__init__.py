from fastapi import HTTPException, status

class CompanyNotFoundError(HTTPException):
    def __init__(self, id: str | None = None, name: str | None = None) -> None:
        if id:
            detail = f"Company with ID {id} not found."
        elif name:
            detail = f"Company with name {name} not found."
        else:
            detail = "Company not found."

        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


class InternalServerError(HTTPException):
    def __init__(self, detail: str = "Internal Server Error.") -> None:
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)


class CompanyControllerException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
