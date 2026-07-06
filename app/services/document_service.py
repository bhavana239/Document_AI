from app.schemas.document import (
    UploadDocumentRequest,
    ProcessDocumentRequest
)

documents = [
    {
        "documentId": "DOC001",
        "machineName": "Automatic Conveyor",
        "fileName": "Mechanical Drawing.pdf",
        "filePath": "/uploads/designs/Mechanical Drawing.pdf",
        "status": "COMPLETED"
    },
    {
        "documentId": "DOC002",
        "machineName": "Panel Board",
        "fileName": "Mechanical Drawing.pdf",
        "filePath": "/uploads/designs/Mechanical Drawing.pdf",
        "status": "PROCESSING"
    },
    {
        "documentId": "DOC003",
        "machineName": "Hydraulic Press",
        "fileName": "Mechanical Drawing.pdf",
        "filePath": "/uploads/designs/Mechanical Drawing.pdf",
        "status": "QUEUED"
    }
]


def upload_document(document: UploadDocumentRequest):

    return {
        "documentId": "DOC004",
        "status": "UPLOADED",
        "message": "Document uploaded successfully",
        "data": document.model_dump()
    }


def process_document(document: ProcessDocumentRequest):

    return {
        "documentId": document.documentId,
        "status": "PROCESSING",
        "message": "Document processing started",
        "steps": [
            "Upload Completed",
            "OCR Queued",
            "AI Processing Started"
        ]
    }


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


def get_document_result(document_id: str):

    for doc in documents:

        if doc["documentId"] == document_id:
            return doc

    return {
        "message": "Document not found"
    }