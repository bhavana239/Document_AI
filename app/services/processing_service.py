import os

from app.services.pdf_service import convert_pdf_to_images
from app.services.image_service import preprocess_image
from app.services.ocr_service import extract_text

from app.services.row_detector import detect_rows
from app.services.column_detector import detect_columns
from app.services.table_builder import build_table
from app.services.header_detector import detect_header

from app.services.qwen_service import parse_bom_with_qwen
from app.services.validation_service import validate_bom_data
from app.services.mapping_service import map_bom_to_erp


def process_document_pipeline(file_path: str):
    """
    New Document AI Pipeline

    PDF/Image
        ↓
    Image Preprocessing
        ↓
    OCR
        ↓
    Row Detection
        ↓
    Column Detection
        ↓
    Table Builder
        ↓
    Header Detection
        ↓
    BOM Parsing
        ↓
    Validation
        ↓
    ERP Mapping
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        images = convert_pdf_to_images(file_path)
    else:
        images = [file_path]

    all_words = []

    final_headers = []

    final_rows = []

    final_metadata = []

    for image in images:

        print(f"Processing : {image}")

        # ----------------------------
        # Step 1 : Image Preprocessing
        # ----------------------------

        processed_image = preprocess_image(image)

        # ----------------------------
        # Step 2 : OCR
        # ----------------------------

        words = extract_text(processed_image)

        all_words.extend(words)

        # ----------------------------
        # Step 3 : Detect Rows
        # ----------------------------

        rows = detect_rows(words)

        # ----------------------------
        # Step 4 : Detect Columns
        # ----------------------------

        column_data = detect_columns(rows)

        # ----------------------------
        # Step 5 : Build Table
        # ----------------------------

        table = build_table(column_data)

        # ----------------------------
        # Step 6 : Detect Header
        # ----------------------------

        table = detect_header(table)

        if not final_headers:
            final_headers = table["headers"]

        final_rows.extend(table["rows"])

        final_metadata.extend(table["metadata"])

    # ----------------------------
# Step 7 : Parse BOM using Qwen
# ----------------------------

    parsed = parse_bom_with_qwen(
    final_headers,
    final_rows
)

    bom_items = parsed["bom"]

    # ----------------------------
    # Step 8 : Validate
    # ----------------------------

    validation = validate_bom_data(bom_items)

    if validation["status"] == "INVALID":

        return {

            "status": "FAILED",

            "pages": len(images),

            "headers": final_headers,

            "rows": final_rows,

            "metadata": final_metadata,

            "parsedBom": bom_items,

            "validation": validation
        }

    # ----------------------------
    # Step 9 : ERP Mapping
    # ----------------------------

    mapped = map_bom_to_erp(bom_items)

    return {

        "status": "SUCCESS",

        "pages": len(images),

        "headers": final_headers,

        "rows": final_rows,

        "metadata": final_metadata,

        "parsedBom": bom_items,

        "validation": validation,

        "erpMapping": mapped
    }