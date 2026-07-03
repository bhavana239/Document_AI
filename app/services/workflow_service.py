def start_workflow(data):

    return {
        "workflowId": "WF001",
        "status": "PENDING_REVIEW",
        "message": "Workflow started successfully",
        "data": data
    }


def approve_workflow(data):

    return {
        "workflowId": "WF001",
        "status": "APPROVED",
        "message": "Workflow approved successfully",
        "data": data
    }