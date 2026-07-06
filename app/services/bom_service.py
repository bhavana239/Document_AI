from app.schemas.bom import (
    CreateBomRequest,
    ValidateBomRequest,
    ApproveBomRequest
)


def validate_bom(bom: ValidateBomRequest):

    if not bom.bomId:
        return {
            "status": "INVALID",
            "errors": [
                "BOM ID is required"
            ]
        }

    return {
        "bomId": bom.bomId,
        "status": "VALID",
        "errors": []
    }


def create_bom(bom: CreateBomRequest):

    return {
        "bomId": "BOM001",
        "status": "DRAFT",
        "message": "Draft BOM created successfully",
        "data": bom.model_dump()
    }


def approve_bom(bom: ApproveBomRequest):

    return {
        "bomId": bom.bomId,
        "status": "APPROVED",
        "message": "BOM approved successfully",
        "approvedBy": bom.approvedBy
    }