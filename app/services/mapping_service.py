def map_bom_to_erp(bom_items: list):
    """
    Maps extracted BOM items to ERP master data.

    Current Version:
        - Simulates Item Master lookup.
        - Determines whether an item already exists.

    Future Version:
        - Query Spring Boot Item Master
        - Query Material Master
        - Query UOM Master
        - Query Vendor Master
        - Return matching results
    """

    mapped_items = []

    # Dummy Item Master
    existing_items = {
        "PLT001": {
            "itemCode": "ITEM001",
            "description": "SS304 Plate"
        },
        "MTR001": {
            "itemCode": "ITEM002",
            "description": "Motor Assembly"
        }
    }

    for item in bom_items:

        part_number = item["partNumber"]

        if part_number in existing_items:

            mapped_items.append({

                "partNumber": part_number,

                "itemCode": existing_items[part_number]["itemCode"],

                "exists": True,

                "description": existing_items[part_number]["description"],

                "quantity": item["quantity"],

                "material": item["material"]
            })

        else:

            mapped_items.append({

                "partNumber": part_number,

                "itemCode": None,

                "exists": False,

                "description": item["description"],

                "quantity": item["quantity"],

                "material": item["material"],

                "action": "CREATE_NEW_ITEM"
            })

    return mapped_items