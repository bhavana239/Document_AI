from pydantic import BaseModel
from typing import List


class BomItem(BaseModel):
    partNumber: str
    description: str
    material: str
    grade: str = ""
    dimensions: str = ""
    quantity: int
    uom: str
    revision: str = ""
    drawingNumber: str = ""
    assemblyHierarchy: str = ""
    notes: str = ""
    finishCoating: str = ""
    manufacturer: str = ""


class CreateBomRequest(BaseModel):
    drawingNumber: str
    revision: str
    createdBy: str = "AI"
    items: List[BomItem]


class ValidateBomRequest(BaseModel):
    bomId: str


class ApproveBomRequest(BaseModel):
    bomId: str
    approvedBy: str


class UpdateBomRequest(BaseModel):
    drawingNumber: str
    revision: str
    items: List[BomItem]


class RejectBomRequest(BaseModel):
    bomId: str
    rejectedBy: str
    reason: str = ""