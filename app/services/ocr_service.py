from paddleocr import PaddleOCR
import numpy as np

# Initialize PaddleOCR once
ocr = PaddleOCR(
    lang="en",
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)


def extract_text(image_path):
    """
    Extract OCR words with spatial information.

    Returns:
    [
        {
            "id": 1,
            "text": "Bolt",
            "confidence": 0.98,
            "page": 1,
            "left": 20,
            "top": 120,
            "right": 180,
            "bottom": 150,
            "width": 160,
            "height": 30,
            "center_x": 100,
            "center_y": 135
        }
    ]
    """

    result = ocr.predict(image_path)

    words = []

    word_id = 1
    page_number = 1

    for page in result:

        texts = page.get("rec_texts", [])
        scores = page.get("rec_scores", [])
        boxes = page.get("rec_boxes", [])

        for text, score, box in zip(texts, scores, boxes):

            # Ignore low-confidence OCR results
            if float(score) < 0.45:
                continue

            # Convert numpy array to list
            if isinstance(box, np.ndarray):
                box = box.tolist()

            # PaddleOCR v3 format: [x1, y1, x2, y2]
            if (
                len(box) == 4 and
                isinstance(box[0], (int, float))
            ):

                left = int(box[0])
                top = int(box[1])
                right = int(box[2])
                bottom = int(box[3])

            # PaddleOCR v2 format: 4 corner points
            else:

                xs = [int(p[0]) for p in box]
                ys = [int(p[1]) for p in box]

                left = min(xs)
                right = max(xs)
                top = min(ys)
                bottom = max(ys)

            width = right - left
            height = bottom - top

            words.append({

                "id": word_id,

                "text": str(text).strip(),

                "confidence": round(float(score), 4),

                "page": page_number,

                "left": left,
                "top": top,
                "right": right,
                "bottom": bottom,

                "width": width,
                "height": height,

                "center_x": left + width // 2,
                "center_y": top + height // 2

            })

            word_id += 1

        page_number += 1

    # Sort by page, Y position, then X position
    words.sort(
        key=lambda w: (
            w["page"],
            w["top"],
            w["left"]
        )
    )

    return words