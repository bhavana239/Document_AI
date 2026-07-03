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
def upload_document(document):

    return {
        "documentId": "DOC004",
        "status": "UPLOADED",
        "message": "Document uploaded successfully",
        "data": document
    }
def process_document(document):

    return {
        "documentId": document.get("documentId"),
        "status": "PROCESSING",
        "message": "Document processing started",
        "steps": [
            "Upload Completed",
            "OCR Queued",
            "AI Processing Started"
        ]
    }