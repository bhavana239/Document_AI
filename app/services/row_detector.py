def detect_rows(words, tolerance=20):
    """
    Group OCR words into rows using center Y coordinate.
    """

    if not words:
        return []

    # Sort words by page, center Y, left
    words = sorted(
        words,
        key=lambda w: (
            w["page"],
            w["center_y"],
            w["left"]
        )
    )

    rows = []

    current_row = []
    current_y = None

    for word in words:

        y = word["center_y"]

        # First word
        if current_y is None:
            current_row = [word]
            current_y = y
            continue

        # Same row
        if abs(y - current_y) <= tolerance:

            current_row.append(word)

            current_y = sum(
                w["center_y"] for w in current_row
            ) / len(current_row)

        else:

            current_row.sort(key=lambda w: w["left"])

            rows.append(current_row)

            current_row = [word]

            current_y = y

    if current_row:
        current_row.sort(key=lambda w: w["left"])
        rows.append(current_row)

    return rows