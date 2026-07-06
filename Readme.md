# Prerequisites

```bash
Python 3.11
```

## Create Virtual Environment

```bash
python -m venv paddle_env
```

## Activate Virtual Environment

```bash
paddle_env\Scripts\activate
```

## Install Backend Dependencies

```bash
pip install fastapi
pip install uvicorn
pip install python-multipart
pip install pydantic
pip install python-dotenv
pip install pymupdf
pip install opencv-python
```

## Install OCR Dependencies

```bash
pip install paddlepaddle==3.1.1
pip install paddleocr
```

## Run Application

```bash
python -m uvicorn app.main:app --reload
```
