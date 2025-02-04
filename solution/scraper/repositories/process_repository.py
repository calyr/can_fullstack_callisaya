# from rq import Queue
from rq import Queue
from typing import List
from sqlalchemy import update

from redis import Redis
from models import  ProcessState, ScraperResponse, ScraperState
from repositories.notify_client import notifyProcessCompleted
from services.scraper import scraping
from settings import process, database
from datetime import datetime
# Configuración de Redis
redis = Redis(host='cache', port=6379, password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81')
queue = Queue('canurl', connection=redis)

# Función que simula el procesamiento de la URL
async def process_url(url: str, processId: str):
    print(f"Procesado: {processId}")
    data_scraping = await scraping(url)
    print(f"Resultado = {data_scraping.state}")
    await update_process(processId=processId, scraperResponse= data_scraping)
    await notifyProcessCompleted(processId=processId)
    return f"Resultado de exito"

async def list(userId: str):
    query = process.select().where(process.c.user_id == userId).order_by(process.c.id)
    return await database.fetch_all(query)

async def create_process(userId: str, urls: List[str]):
    
    timestamp = datetime.now()
    for url in urls:
        query = process.insert().values(
            start_date=timestamp,
            end_date=None,
            timestamp=timestamp,
            state = ProcessState.EN_PROCESO,
            user_id=str(userId),
            url=url,
            observation=""
            ).returning(process.c.id)
        processId = await database.execute(query)
        queue.enqueue(process_url, url, processId)
    return userId

async def update_process(processId: str, scraperResponse: ScraperResponse):
    observation = scraperResponse.FAILED if scraperResponse.state == ScraperState.FAILED else ""
    if not database.is_connected:  # Verifica conexión antes de ejecutar la query
        await database.connect()
    query = (
        update(process)
        .where(process.c.id == processId)  
        .values(
            state=ProcessState.COMPLETADO,
            observation=observation ,
            content_scraping=scraperResponse.content,
            end_date=datetime.now(),
            title_scraping = scraperResponse.title,
            date_scraping = scraperResponse.date
        )
    )
    await database.execute(query)