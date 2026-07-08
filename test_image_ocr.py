from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en')

result = ocr.predict("sample image1.png")

print(result)