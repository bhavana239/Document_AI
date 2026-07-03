from fastapi import APIRouter
from app.services.bom_service import (
    validate_bom,
    create_bom,
    approve_bom
)

router = APIRouter(
    prefix="/api/bom",
    tags=["BOM"]
)

@router.post("/validate")
def validate(bom: dict):
    return validate_bom(bom)


@router.post("/create")
def create(bom: dict):
    return create_bom(bom)


@router.post("/approve")
def approve(bom: dict):
    return approve_bom(bom)