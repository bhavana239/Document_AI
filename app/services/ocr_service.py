from paddleocr import PaddleOCR

# Load OCR model once
ocr = PaddleOCR(lang='en')


def extract_text(image_path):

    result = ocr.predict(image_path)

    texts = []

    for page in result:
        if "rec_texts" in page:
            texts.extend(page["rec_texts"])

    return texts