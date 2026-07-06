from fastapi import APIRouter
from app.services.workflow_service import (
    start_workflow,
    approve_workflow
)

from app.schemas.workflow import (
    StartWorkflowRequest,
    ApproveWorkflowRequest
)

router = APIRouter(
    prefix="/api/workflow",
    tags=["Workflow"]
)


@router.post("/start")
def start(data: StartWorkflowRequest):
    return start_workflow(data)


@router.post("/approve")
def approve(data: ApproveWorkflowRequest):
    return approve_workflow(data)