from fastapi import FastAPI, Request
from typing import List
from fastapi.responses import JSONResponse
from exception_handlers import invalid_notifier_type_exception_handler
from models import InvalidNotifierTypeException, NotifierModel
from strategy import EMAILNotificator, Notificator, SMSNotificator


app = FastAPI()
#registrando las exceptiones personalizadas
app.add_exception_handler(InvalidNotifierTypeException,invalid_notifier_type_exception_handler)

notifiers_db: List[NotifierModel] = []

@app.get("/")
async def root():
    return { "message": "Peru wait for me.From Bolivia"}

@app.post("/notify")
async def notify(request: Request, notifierModel: NotifierModel):
    

    if notifierModel.type == "email":
        notificator = Notificator(EMAILNotificator())
    elif notifierModel.type == "sms":
        notificator = Notificator(SMSNotificator())
    elif notifierModel.type == "push":
        raise InvalidNotifierTypeException(message="La notificación push aun no esta implementada")
    else:
        raise InvalidNotifierTypeException()
    notificator.send(notifierModel.processId)

    return JSONResponse(
        content={"message": "Se envio la notificación"}
    )