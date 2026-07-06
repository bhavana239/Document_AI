from fastapi import APIRouter
from app.services.bom_service import (
    validate_bom,
    create_bom,
    approve_bom
)
from app.schemas.bom import (
    CreateBomRequest,
    ValidateBomRequest,
    ApproveBomRequest
)

router = APIRouter(
    prefix="/api/bom",
    tags=["BOM"]
)

@router.post("/validate")
def validate(bom: ValidateBomRequest):
    return validate_bom(bom)


@router.post("/create")
def create(bom: CreateBomRequest):
    return create_bom(bom)


@router.post("/approve")
def approve(bom: ApproveBomRequest):
    return approve_bom(bom)