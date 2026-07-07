import re


def detect_header(table):
    """
    Detects the most probable header row.

    Input:
    {
        "headers": [],
        "rows": [],
        "metadata": []
    }

    Output:
    {
        "headers": [...],
        "rows": [...],
        "metadata": [...]
    }
    """

    all_rows = []

    if table.get("headers"):
        all_rows.append(table["headers"])

    all_rows.extend(table.get("rows", []))
    all_rows.extend(table.get("metadata", []))

    if not all_rows:
        return table

    best_score = -999
    best_index = -1

    for index, row in enumerate(all_rows):

        score = 0

        for cell in row:

            cell = str(cell).strip()

            if cell == "":
                continue

            # Numeric → likely data
            if re.fullmatch(r"\d+(\.\d+)?", cell):
                score -= 2

            # Long text → likely description
            elif len(cell) > 15:
                score += 1

            # Short alphabetic text → likely header
            elif re.fullmatch(r"[A-Za-z .#/-]+", cell):
                score += 3

            else:
                score += 1

        if score > best_score:
            best_score = score
            best_index = index

    header = all_rows[best_index]

    data_rows = []
    metadata_rows = []

    for index, row in enumerate(all_rows):

        if index == best_index:
            continue

        first = ""

        for cell in row:

            if str(cell).strip():

                first = str(cell).strip()

                break

        if re.fullmatch(r"\d+", first):
            data_rows.append(row)
        else:
            metadata_rows.append(row)

    return {

        "headers": header,

        "rows": data_rows,

        "metadata": metadata_rows

    }