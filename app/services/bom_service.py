def validate_bom(bom):

    errors = []

    if not bom.get("partNumber"):
        errors.append("Part number is required")

    if not bom.get("material"):
        errors.append("Material is required")

    if not bom.get("quantity"):
        errors.append("Quantity is required")

    if not bom.get("uom"):
        errors.append("Unit of Measure is required")

    if len(errors) == 0:
        return {
            "status": "VALID",
            "errors": []
        }

    return {
        "status": "INVALID",
        "errors": errors
    }
def create_bom(bom):

    return {
        "bomId": "BOM001",
        "status": "DRAFT",
        "message": "Draft BOM created successfully",
        "data": bom
    }
def approve_bom(bom):

    return {
        "bomId": "BOM001",
        "status": "APPROVED",
        "message": "BOM approved successfully",
        "data": bom
    }