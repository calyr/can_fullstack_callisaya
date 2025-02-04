from typing import List
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session

from models import ProcessResponse
from services import upload_service

router = APIRouter()

@router.get("/process/{userId}", response_model=List[ProcessResponse])
async def get_process(userId: str):
    return await upload_service.list(userId)

@router.post("/upload")
async def upload(
  file: UploadFile = File(...),
  userId: str = Form(...)
):
    if not file:
        raise HTTPException(
            status_code=400,
            detail= "Not file provided"
        )
    return await upload_service.save(file, user_id= userId)