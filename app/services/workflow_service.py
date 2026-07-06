from app.schemas.workflow import (
    StartWorkflowRequest,
    ApproveWorkflowRequest
)


def start_workflow(data: StartWorkflowRequest):

    return {
        "workflowId": "WF001",
        "status": "PENDING_REVIEW",
        "message": "Workflow started successfully",
        "data": data.model_dump()
    }


def approve_workflow(data: ApproveWorkflowRequest):

    return {
        "workflowId": data.workflowId,
        "status": "APPROVED",
        "message": "Workflow approved successfully",
        "approvedBy": data.approvedBy
    }