import os

from app.services.pdf_service import convert_pdf_to_images
from app.services.image_service import preprocess_image
from app.services.ocr_service import extract_text
from app.services.layout_service import detect_layout
from app.services.table_service import extract_bom_table
from app.services.bom_parser import parse_bom
from app.services.validation_service import validate_bom_data
from app.services.mapping_service import map_bom_to_erp


def process_document_pipeline(file_path: str):
    """
    Complete Document Processing Pipeline

    Pipeline:
        Upload
            ↓
        PDF Conversion
            ↓
        Image Preprocessing
            ↓
        OCR
            ↓
        Layout Detection
            ↓
        Table Extraction
            ↓
        BOM Parsing
    """

    extension = os.path.splitext(file_path)[1].lower()

    images = []

    # PDF Processing
    if extension == ".pdf":
        images = convert_pdf_to_images(file_path)

    # Image Processing
    else:
        images.append(file_path)

    all_texts = []

    all_layouts = []

    all_tables = []

    all_bom_items = []

    for image in images:

        print(f"Processing : {image}")

        # Step 1
        ocr_ready_image = preprocess_image(image)

        # Step 2
        texts = extract_text(ocr_ready_image)

        all_texts.extend(texts)

        # Step 3
        layout = detect_layout(texts)

        all_layouts.append(layout)

        # Step 4
        table = extract_bom_table(layout)

        all_tables.extend(table)

    # Step 5 - Parse BOM
    parsed_bom = parse_bom(all_tables)

    all_bom_items.extend(parsed_bom["bom"])

    # Step 6 - Validation
    validation = validate_bom_data(all_bom_items)

    if validation["status"] == "INVALID":
        return {
            "status": "FAILED",
            "pages": len(images),
            "validation": validation,
            "parsedBom": all_bom_items
        }

    # Step 7 - ERP Mapping
    mapped_items = map_bom_to_erp(all_bom_items)

    return {
        "status": "SUCCESS",
        "pages": len(images),
        "ocrText": all_texts,
        "layout": all_layouts,
        "table": all_tables,
        "parsedBom": all_bom_items,
        "validation": validation,
        "erpMapping": mapped_items
    }