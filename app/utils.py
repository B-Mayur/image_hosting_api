import uuid
from datetime import datetime
from fastapi import HTTPException
import os

def generate_filename(extension: str) -> str:
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    return f"{timestamp}_{uuid.uuid4().hex}.{extension}"

def validate_image_extension(filename: str) -> str:
    if "." not in filename:
        raise HTTPException(status_code=400, detail="File must have an extension.")
    ext = filename.rsplit(".", 1)[-1].lower()
    if ext not in ["jpg", "jpeg", "png"]:
        raise HTTPException(status_code=400, detail="Unsupported file format.")
    return ext
