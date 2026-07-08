from fastapi import APIRouter, HTTPException, status
from app.services.bom_service import (
    validate_bom,
    create_bom,
    approve_bom,
    update_bom,
    reject_bom,
    get_bom,
    list_boms
)
from app.schemas.bom import (
    CreateBomRequest,
    ValidateBomRequest,
    ApproveBomRequest,
    UpdateBomRequest,
    RejectBomRequest
)

router = APIRouter(
    prefix="/api/bom",
    tags=["BOM"]
)


@router.get("")
def get_all_boms():
    return list_boms()


@router.get("/{bom_id}")
def get_single_bom(bom_id: str):
    bom = get_bom(bom_id)
    if not bom:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"BOM with ID {bom_id} not found"
        )
    return bom


@router.post("/validate")
def validate(bom: ValidateBomRequest):
    return validate_bom(bom)


@router.post("/create")
def create(bom: CreateBomRequest):
    return create_bom(bom)


@router.put("/{bom_id}")
def update(bom_id: str, bom: UpdateBomRequest):
    updated = update_bom(bom_id, bom)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"BOM with ID {bom_id} not found"
        )
    return updated


@router.post("/approve")
def approve(bom: ApproveBomRequest):
    res = approve_bom(bom)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"BOM with ID {bom.bomId} not found in draft database"
        )
    return res


@router.post("/reject")
def reject(bom: RejectBomRequest):
    res = reject_bom(bom)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"BOM with ID {bom.bomId} not found in draft database"
        )
    return res