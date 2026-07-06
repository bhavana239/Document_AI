import os
import fitz  # PyMuPDF


def convert_pdf_to_images(pdf_path: str):

    """
    Converts every page of a PDF into PNG images.

    Returns:
        List of generated image paths.
    """

    document = fitz.open(pdf_path)

    image_folder = "temp/pdf_images"

    os.makedirs(image_folder, exist_ok=True)

    image_paths = []

    for page_number in range(len(document)):

        page = document.load_page(page_number)

        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))

        image_path = os.path.join(
            image_folder,
            f"page_{page_number + 1}.png"
        )

        pix.save(image_path)

        image_paths.append(image_path)

    document.close()

    return image_paths