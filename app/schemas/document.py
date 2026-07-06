from pydantic import BaseModel

class DocumentResponse(BaseModel):

    documentId: str
    status: str
    message: str

class ProcessDocumentRequest(BaseModel):

    documentId: str

class UploadDocumentRequest(BaseModel):

    machineName: str
    documentType: str
    uploadedBy: str