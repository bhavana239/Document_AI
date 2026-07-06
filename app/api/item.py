from fastapi import APIRouter

from app.services.item_service import (
    search_item,
    create_item
)

from app.schemas.item import (
    CreateItemRequest 
)

router = APIRouter(
    prefix="/api/item",
    tags=["Item"]
)


@router.get("/search/{part_number}")
def search(part_number: str):
    return search_item(part_number)

@router.post("/create")
def create(item: CreateItemRequest):
    return create_item(item)