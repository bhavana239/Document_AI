from fastapi import APIRouter
from app.services.workflow_service import (
    start_workflow,
    approve_workflow
)

router = APIRouter(
    prefix="/api/workflow",
    tags=["Workflow"]
)


@router.post("/start")
def start(data: dict):
    return start_workflow(data)


@router.post("/approve")
def approve(data: dict):
    return approve_workflow(data)