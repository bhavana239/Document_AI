

from fastapi import FastAPI
from app.api.document import router
from app.api.bom import router as bom_router
from app.api.item import router as item_router
from app.api.workflow import router as workflow_router
from app.api.ocr import router as ocr_router

app = FastAPI(
    title="Document AI Service"
)

app.include_router(router)
app.include_router(bom_router)
app.include_router(item_router)
app.include_router(workflow_router)
app.include_router(ocr_router)