from pydantic import BaseModel

class StartWorkflowRequest(BaseModel):

    documentId: str
    workflowName: str

class ApproveWorkflowRequest(BaseModel):

    workflowId: str
    approvedBy: str