def detect_layout(ocr_texts):

    layout = {
        "titleBlock": [],
        "tables": [],
        "notes": [],
        "dimensions": []
    }

    for text in ocr_texts:

        value = text.upper()

        if "DWG" in value or "DRAWING" in value:
            layout["titleBlock"].append(text)

        elif "REV" in value:
            layout["titleBlock"].append(text)

        elif "NOTE" in value:
            layout["notes"].append(text)

        elif "MM" in value or "Ø" in value:
            layout["dimensions"].append(text)

        else:
            layout["tables"].append(text)

    return layout