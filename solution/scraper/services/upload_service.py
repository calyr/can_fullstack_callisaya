from fastapi import UploadFile
from repositories import process_repository

async def list(userId: str):
    return await process_repository.list(userId)

async def save(file: UploadFile, user_id: str):
   
    urls = await readFileTxt(file)
    await process_repository.create_process(user_id, urls)
    return {
        "total_lines": len(urls),
        "lines": urls,
    }

async def readFileTxt(file: UploadFile):
    contents = (await file.read()).decode("utf-8")
    return contents.splitlines()


