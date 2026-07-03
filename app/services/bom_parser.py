def parse_bom(texts):

    # Remove table headers
    headers = [
        "Part No.",
        "Name",
        "Material",
        "Qty"
    ]

    filtered = []

    for text in texts:
        if text not in headers:
            filtered.append(text)

    bom = []

    # Every BOM row contains:
    # Part Number, Description, Material, Quantity
    for i in range(0, len(filtered), 4):

        if i + 3 < len(filtered):

            try:
                quantity = int(filtered[i + 3])
            except:
                quantity = 0

            bom.append({
                "partNumber": filtered[i],
                "description": filtered[i + 1],
                "material": filtered[i + 2],
                "quantity": quantity
            })

    return {
        "bom": bom
    }