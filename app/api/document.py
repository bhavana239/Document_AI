from fastapi import APIRouter

from app.services.document_service import (
    upload_document,
    process_document
)
router = APIRouter(
    prefix="/api/document",
    tags=["Document"]
)


@router.get("/status/{document_id}")
def get_document_status(document_id: str):

    for doc in documents:
        if doc["documentId"] == document_id:
            return {
                "documentId": doc["documentId"],
                "status": doc["status"]
            }

    return {
        "message": "Document not found"
    }


@router.get("/result/{document_id}")
def get_document_result(document_id: str):

    for doc in documents:
        if doc["documentId"] == document_id:
            return doc

    return {
        "message": "Document not found"
    }


@router.post("/upload")
def upload(document: dict):
    return upload_document(document)

@router.post("/process")
def process(document: dict):
    return process_document(document)