from typing import List


def validate_bom_data(bom_items: List[dict]):
    """
    Dynamic validation.

    Validates every extracted field without assuming
    Part Number, Description, Material, Quantity, etc.
    """

    errors = []
    warnings = []

    if not bom_items:

        return {
            "status": "INVALID",
            "errors": ["No BOM rows extracted."],
            "warnings": []
        }

    duplicate_check = {}

    for row_number, row in enumerate(bom_items, start=1):

        if not isinstance(row, dict):

            errors.append(
                f"Row {row_number}: Invalid row format."
            )
            continue

        # Validate every extracted column
        for column_name, value in row.items():

            # Empty value
            if value is None:

                warnings.append(
                    f"Row {row_number}: '{column_name}' is NULL."
                )

                continue

            if isinstance(value, str):

                value = value.strip()

                if value == "":

                    warnings.append(
                        f"Row {row_number}: '{column_name}' is empty."
                    )

        # Duplicate row detection
        row_signature = tuple(sorted(row.items()))

        if row_signature in duplicate_check:

            warnings.append(
                f"Duplicate row detected ({row_number})."
            )

        else:

            duplicate_check[row_signature] = row_number

    status = "VALID"

    if errors:
        status = "INVALID"

    return {
        "status": status,
        "errors": errors,
        "warnings": warnings
    }