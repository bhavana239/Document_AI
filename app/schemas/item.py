from pydantic import BaseModel

class CreateItemRequest(BaseModel):
    partNumber: str
    description: str
    material: str
    quantity: int
    uom: str