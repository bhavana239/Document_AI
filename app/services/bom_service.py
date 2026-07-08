import uuid
from datetime import datetime
from typing import Dict, Any

from app.schemas.bom import (
    CreateBomRequest,
    ValidateBomRequest,
    ApproveBomRequest,
    UpdateBomRequest,
    RejectBomRequest
)

# Simulated in-memory database tables
draft_boms_db: Dict[str, Any] = {}  # Stores DRAFT, UNDER_REVIEW, and REJECTED BOMs
final_boms_db: Dict[str, Any] = {}  # Stores APPROVED (Final) BOMs


def validate_bom(bom: ValidateBomRequest):
    if not bom.bomId:
        return {
            "status": "INVALID",
            "errors": [
                "BOM ID is required"
            ]
        }

    # Fetch BOM to check if it exists and is valid
    existing_bom = get_bom(bom.bomId)
    if not existing_bom:
        return {
            "status": "INVALID",
            "errors": [
                f"BOM with ID {bom.bomId} not found"
            ]
        }

    return {
        "bomId": bom.bomId,
        "status": "VALID",
        "errors": []
    }


def create_bom(bom: CreateBomRequest):
    bom_id = f"BOM-{str(uuid.uuid4())[:8].upper()}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    draft_bom = {
        "bomId": bom_id,
        "status": "DRAFT",
        "reviewStatus": "PENDING_REVIEW",
        "createdBy": bom.createdBy,
        "createdAt": timestamp,
        "drawingNumber": bom.drawingNumber,
        "revision": bom.revision,
        "items": [item.model_dump() for item in bom.items],
        "history": [
            {
                "action": "CREATED",
                "status": "DRAFT",
                "reviewStatus": "PENDING_REVIEW",
                "user": bom.createdBy,
                "timestamp": timestamp,
                "details": "Draft BOM created from ERP Mapping."
            }
        ]
    }

    # Save to in-memory store
    draft_boms_db[bom_id] = draft_bom

    return {
        "message": "Draft BOM created successfully",
        "draftBom": draft_bom
    }


def update_bom(bom_id: str, bom: UpdateBomRequest):
    if bom_id not in draft_boms_db:
        return None

    existing_bom = draft_boms_db[bom_id]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Perform update
    existing_bom["drawingNumber"] = bom.drawingNumber
    existing_bom["revision"] = bom.revision
    existing_bom["items"] = [item.model_dump() for item in bom.items]
    existing_bom["status"] = "UNDER_REVIEW"

    # Log history
    existing_bom["history"].append({
        "action": "UPDATED",
        "status": "UNDER_REVIEW",
        "reviewStatus": existing_bom["reviewStatus"],
        "user": "Engineer",
        "timestamp": timestamp,
        "details": "BOM items and details updated during engineer review."
    })

    draft_boms_db[bom_id] = existing_bom
    return existing_bom


def approve_bom(bom: ApproveBomRequest):
    bom_id = bom.bomId
    if bom_id not in draft_boms_db:
        return None

    existing_bom = draft_boms_db[bom_id]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update status to approved
    existing_bom["status"] = "APPROVED"
    existing_bom["reviewStatus"] = "APPROVED"
    existing_bom["history"].append({
        "action": "APPROVED",
        "status": "APPROVED",
        "reviewStatus": "APPROVED",
        "user": bom.approvedBy,
        "timestamp": timestamp,
        "details": f"BOM approved by {bom.approvedBy}."
    })

    # Move to final BOM storage
    final_boms_db[bom_id] = existing_bom
    draft_boms_db.pop(bom_id, None)

    return {
        "bomId": bom_id,
        "status": "APPROVED",
        "message": "BOM approved successfully",
        "approvedBy": bom.approvedBy,
        "bom": existing_bom
    }


def reject_bom(bom: RejectBomRequest):
    bom_id = bom.bomId
    if bom_id not in draft_boms_db:
        return None

    existing_bom = draft_boms_db[bom_id]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update status to rejected
    existing_bom["status"] = "REJECTED"
    existing_bom["reviewStatus"] = "REJECTED"
    existing_bom["history"].append({
        "action": "REJECTED",
        "status": "REJECTED",
        "reviewStatus": "REJECTED",
        "user": bom.rejectedBy,
        "timestamp": timestamp,
        "details": f"BOM rejected by {bom.rejectedBy}. Reason: {bom.reason}" if bom.reason else f"BOM rejected by {bom.rejectedBy}."
    })

    draft_boms_db[bom_id] = existing_bom

    return {
        "bomId": bom_id,
        "status": "REJECTED",
        "message": "BOM rejected successfully",
        "rejectedBy": bom.rejectedBy,
        "bom": existing_bom
    }


def get_bom(bom_id: str):
    if bom_id in draft_boms_db:
        return draft_boms_db[bom_id]
    if bom_id in final_boms_db:
        return final_boms_db[bom_id]
    return None


def list_boms():
    return {
        "draftBoms": list(draft_boms_db.values()),
        "finalBoms": list(final_boms_db.values())
    }