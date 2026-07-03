from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.services.ocr_service import extract_text
from app.services.bom_parser import parse_bom

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

    texts = extract_text(file_path)

    parsed_bom = parse_bom(texts)

    return {
        "status": "SUCCESS",
        "fileName": file.filename,
        "texts": texts,
        "parsedBom": parsed_bom
    }