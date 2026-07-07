import cv2
import os


def preprocess_image(image_path: str):

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        raise Exception(f"Unable to read image : {image_path}")

    # -------------------------------
    # Step 1 : Resize
    # -------------------------------
    height, width = image.shape[:2]

    if width < 1800:
        scale = 1800 / width

        image = cv2.resize(
            image,
            None,
            fx=scale,
            fy=scale,
            interpolation=cv2.INTER_CUBIC
        )

    # -------------------------------
    # Step 2 : Gray Scale
    # -------------------------------
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # -------------------------------
    # Step 3 : Noise Removal
    # -------------------------------
    gray = cv2.GaussianBlur(
        gray,
        (3, 3),
        0
    )

    # -------------------------------
    # Step 4 : Adaptive Threshold
    # -------------------------------
    binary = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        15
    )

    # -------------------------------
    # Step 5 : Save processed image
    # -------------------------------
    os.makedirs("temp", exist_ok=True)

    output_path = os.path.join(
        "temp",
        os.path.basename(image_path)
    )

    cv2.imwrite(output_path, binary)

    return output_path