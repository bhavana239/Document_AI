def extract_bom_table(layout: dict):

    """
    Extract only the BOM table
    from the detected layout.
    """

    if "tables" not in layout:
        return []

    table_data = layout["tables"]

    headers = {
        "PART NO",
        "PART NUMBER",
        "DESCRIPTION",
        "NAME",
        "MATERIAL",
        "QTY",
        "QUANTITY"
    }

    filtered = []

    for text in table_data:

        value = text.strip()

        if value.upper() in headers:
            continue

        filtered.append(value)

    return filtered