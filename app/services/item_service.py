items = [
    {
        "itemCode": "ITEM001",
        "partNumber": "PLT001",
        "description": "SS304 Plate"
    },
    {
        "itemCode": "ITEM002",
        "partNumber": "MTR001",
        "description": "Motor Assembly"
    }
]


def search_item(part_number):

    for item in items:
        if item["partNumber"] == part_number:
            return {
                "found": True,
                "item": item
            }

    return {
        "found": False,
        "message": "Item not found"
    }
def create_item(item):

    return {
        "itemCode": "ITEM003",
        "status": "CREATED",
        "message": "Item created successfully",
        "data": item
    }