from typing import List


def validate_bom_data(bom_items: List[dict]):
    """
    Validate extracted BOM data before sending it to ERP.

    Returns:
        {
            "status": "VALID" | "INVALID",
            "errors": [...],
            "warnings": [...]
        }
    """

    errors = []
    warnings = []

    part_numbers = set()

    for index, item in enumerate(bom_items, start=1):

        part_number = item.get("partNumber")
        description = item.get("description")
        material = item.get("material")
        quantity = item.get("quantity")

        # Required Fields
        if not part_number:
            errors.append(
                f"Row {index}: Part Number is required."
            )

        if not description:
            errors.append(
                f"Row {index}: Description is required."
            )

        if not material:
            errors.append(
                f"Row {index}: Material is required."
            )

        # Quantity Validation
        if quantity is None:
            errors.append(
                f"Row {index}: Quantity is missing."
            )

        elif quantity <= 0:
            errors.append(
                f"Row {index}: Quantity should be greater than zero."
            )

        # Duplicate Check
        if part_number:

            if part_number in part_numbers:
                warnings.append(
                    f"Duplicate Part Number : {part_number}"
                )

            else:
                part_numbers.add(part_number)

    status = "VALID"

    if errors:
        status = "INVALID"

    return {
        "status": status,
        "errors": errors,
        "warnings": warnings
    }