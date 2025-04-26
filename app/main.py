from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os

from .config import config
from .logger import logger
from .utils import generate_filename, validate_image_extension

app = FastAPI(title="Local Image Hosting API")

UPLOAD_DIR = config["upload_dir"]
os.makedirs(UPLOAD_DIR, exist_ok=True)

app.mount("/images", StaticFiles(directory=UPLOAD_DIR), name="images")

@app.get("/")
async def root():
    return {"message": "Image Hosting API is live! Use /upload to upload images."}


@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        ext = validate_image_extension(file.filename)
        filename = generate_filename(ext)
        file_path = os.path.join(UPLOAD_DIR, filename)

        contents = await file.read()
        with open(file_path, "wb") as f:
            f.write(contents)

        public_url = f"/images/{filename}"
        full_url = f"{config['base_url']}{public_url}"
        logger.info(f"Image uploaded successfully: {filename}")
        return {"url": full_url}

    except HTTPException as e:
        logger.warning(f"Upload failed: {e.detail}")
        raise
    except Exception as e:
        logger.exception("Unexpected error during upload")
        raise HTTPException(status_code=500, detail="Internal server error")
