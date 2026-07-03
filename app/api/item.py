from fastapi import APIRouter

from app.services.item_service import (
    search_item,
    create_item
)

router = APIRouter(
    prefix="/api/item",
    tags=["Item"]
)


@router.get("/search/{part_number}")
def search(part_number: str):
    return search_item(part_number)

@router.post("/create")
def create(item: dict):
    return create_item(item)