def detect_columns(rows, tolerance=80):
    """
    Detect columns using the widest row as reference.
    """

    if not rows:
        return {
            "columns": [],
            "rows": []
        }

    # ----------------------------------------
    # Find reference row (maximum cells)
    # ----------------------------------------

    reference_row = max(
        rows,
        key=lambda r: len(r)
    )

    # ----------------------------------------
    # Column positions
    # ----------------------------------------

    column_positions = sorted([
        word["center_x"]
        for word in reference_row
    ])

    # Remove duplicate columns

    merged_columns = []

    for x in column_positions:

        if not merged_columns:
            merged_columns.append(x)
            continue

        if abs(x - merged_columns[-1]) <= tolerance:

            merged_columns[-1] = int(
                (merged_columns[-1] + x) / 2
            )

        else:

            merged_columns.append(x)

    column_positions = merged_columns

    # ----------------------------------------
    # Build rows
    # ----------------------------------------

    table_rows = []

    for row in rows:

        values = [""] * len(column_positions)

        for word in row:

            x = word["center_x"]

            nearest = min(
                range(len(column_positions)),
                key=lambda i: abs(
                    column_positions[i] - x
                )
            )

            if values[nearest]:

                values[nearest] += " " + word["text"]

            else:

                values[nearest] = word["text"]

        table_rows.append(values)

    return {

        "columns": column_positions,

        "rows": table_rows

    }