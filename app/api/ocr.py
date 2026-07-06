from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.services.processing_service import process_document_pipeline

router = APIRouter(
    prefix="/api/document",
    tags=["Document OCR"]
)

@router.post("/extract")
async def extract_document(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return process_document_pipeline(file_path)