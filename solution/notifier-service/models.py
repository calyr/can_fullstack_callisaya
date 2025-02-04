from enum import Enum
from pydantic import BaseModel

class NotifierType(str, Enum):
    emai = "email"
    sms = "sms"
    push = "push"
    sat = "sat"

class NotifierModel(BaseModel):
    processId: str
    type: NotifierType

class InvalidNotifierTypeException(Exception):
    def __init__(self, message: str):
        self.message = message

class ErrorResponse(BaseModel):
    detail: str