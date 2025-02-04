# from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


# Base = declarative_base()

class ProcessState(str, Enum):
    EN_PROCESO = "in progress"
    COMPLETADO = "completed"

class ProcessResponse(BaseModel):
    id: int
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    timestamp: Optional[datetime] = Field(None, alias="timestamp", description="Fecha y hora del registro")
    state: str
    user_id: str
    url: str
    observation: str
    content_scraping: Optional[str]=None
    title_scraping: Optional[str]=None
    date_scraping: Optional[str]=None

class ScraperState(str, Enum):
    COMPLEADO = "Completed"
    FAILED = "Failed"

class ScraperResponse:
    url: str = "N/E"
    title: str = "N/E"
    date: str = "N/E"
    content: str= "N/E"
    state: ScraperState = ""

class NotifierType(Enum):
    email = "email"
    sms = "sms"
    push_notification = "push_notification"
    sat = "sat"