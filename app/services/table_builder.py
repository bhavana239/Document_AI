import re


def build_table(column_data):
    """
    Builds a generic table from detected columns.

    Input:
    {
        "columns":[...],
        "rows":[
            [...],
            [...]
        ]
    }

    Output:
    {
        "headers": [],
        "rows": [],
        "metadata": []
    }
    """

    rows = column_data["rows"]

    if not rows:
        return {
            "headers": [],
            "rows": [],
            "metadata": []
        }

    header_candidates = []

    data_rows = []

    metadata_rows = []

    # -----------------------------------
    # Analyse every row
    # -----------------------------------

    for row in rows:

        non_empty = [cell.strip() for cell in row if cell.strip()]

        if len(non_empty) == 0:
            continue

        numeric = 0

        alphabetic = 0

        for cell in non_empty:

            if re.fullmatch(r"\d+(\.\d+)?", cell):
                numeric += 1
            else:
                alphabetic += 1

        header_score = alphabetic * 2 - numeric

        header_candidates.append({

            "row": row,

            "score": header_score

        })

    # -----------------------------------
    # Select Best Header
    # -----------------------------------

    best_header = max(
        header_candidates,
        key=lambda x: x["score"]
    )

    headers = best_header["row"]

    # -----------------------------------
    # Split rows
    # -----------------------------------

    for row in rows:

        if row == headers:
            continue

        first = ""

        for cell in row:

            if cell.strip():

                first = cell.strip()

                break

        if re.fullmatch(r"\d+", first):

            data_rows.append(row)

        else:

            metadata_rows.append(row)

    return {

        "headers": headers,

        "rows": data_rows,

        "metadata": metadata_rows

    }