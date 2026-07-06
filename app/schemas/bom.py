from pydantic import BaseModel

class CreateBomRequest(BaseModel):

    drawingNumber: str
    revision: str
    createdBy: str

class ValidateBomRequest(BaseModel):

    bomId: str

class ApproveBomRequest(BaseModel):

    bomId: str
    approvedBy: str