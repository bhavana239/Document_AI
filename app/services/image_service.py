import os
import cv2
import numpy as np


def preprocess_image(image_path: str) -> str:
    """
    Preprocess image before OCR.

    Steps:
    1. Read Image
    2. Convert to Grayscale
    3. Remove Noise
    4. Improve Contrast
    5. Thresholding
    6. Save Processed Image

    Returns:
        Processed image path
    """

    image = cv2.imread(image_path)

    if image is None:
        raise Exception(f"Unable to read image : {image_path}")

    # Convert to Gray
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Remove Noise
    denoise = cv2.fastNlMeansDenoising(gray)

    # Improve Contrast
    contrast = cv2.equalizeHist(denoise)

    # Binary Threshold
    processed = cv2.adaptiveThreshold(
        contrast,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        10
    )

    output_folder = "temp/processed_images"

    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(
        output_folder,
        os.path.basename(image_path)
    )

    cv2.imwrite(output_path, processed)

    return output_path