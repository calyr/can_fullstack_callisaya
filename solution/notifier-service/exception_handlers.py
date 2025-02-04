from fastapi import Request
from fastapi.responses import JSONResponse

from models import InvalidNotifierTypeException

async def invalid_notifier_type_exception_handler( request: Request, exc: InvalidNotifierTypeException):
    return JSONResponse(
        status_code=400,
        content = { "detail": exc.message }
    )