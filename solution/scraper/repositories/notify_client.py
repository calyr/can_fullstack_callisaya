import httpx
import json
from models import NotifierType

async def notifyProcessCompleted(processId: str):
    async with httpx.AsyncClient() as client:
        data = {
            "processId": str(processId),
            "type": NotifierType.email.value
        }
        response = await client.post("http://notifier-service:8000/notify", json=data)
        response_data = {
            "status_code": response.status_code,
            "headers": dict(response.headers),  # Convertir los encabezados a un diccionario
            "json_body": response.json() if response.headers.get('Content-Type') == 'application/json' else response.text  # Verifica si el cuerpo es JSON
        }

        
        if response.status_code == 200:
            print(f'NOTIFIY CLIENT processId= {processId}')    
            return {"error": 0, "message" : "Notificación enviada exitosamente."}
        else:
            print(json.dumps(response_data, indent=4))
            print(f'NOTIFIY CLIENT ERROR processId= {processId}') 
            return {"error": 1, "mesage": "No se pudo enviar la notifcación."}

