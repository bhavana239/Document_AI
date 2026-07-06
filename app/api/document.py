from fastapi import APIRouter

from app.services.document_service import (
    upload_document,
    process_document,
    get_document_status,
    get_document_result
)

from app.schemas.document import (
    UploadDocumentRequest,
    ProcessDocumentRequest
)

router = APIRouter(
    prefix="/api/document",
    tags=["Document"]
)


@router.get("/status/{document_id}")
def document_status(document_id: str):
    return get_document_status(document_id)


@router.get("/result/{document_id}")
def document_result(document_id: str):
    return get_document_result(document_id)


@router.post("/upload")
def upload(document: UploadDocumentRequest):
    return upload_document(document)

@router.post("/process")
def process(document: ProcessDocumentRequest):
    return process_document(document)