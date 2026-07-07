def parse_bom(table):
    """
    Generic BOM Parser

    Input:
    {
        "headers": [...],
        "rows": [...]
    }

    Output:
    {
        "headers": [...],
        "bom": [...]
    }
    """

    headers = table.get("headers", [])
    rows = table.get("rows", [])

    bom = []

    # Header exists
    if headers:

        for row in rows:

            item = {}

            for index, value in enumerate(row):

                if index < len(headers):
                    header = headers[index].strip()

                    if header == "":
                        header = f"Column_{index + 1}"

                else:
                    header = f"Column_{index + 1}"

                # Prevent duplicate headers
                header_name = header
                counter = 1

                while header_name in item:
                    counter += 1
                    header_name = f"{header}_{counter}"

                item[header_name] = value

            bom.append(item)

    # No headers
    else:

        for row in rows:

            item = {}

            for index, value in enumerate(row):
                item[f"Column_{index + 1}"] = value

            bom.append(item)

    return {
        "headers": headers,
        "bom": bom
    }