# backend/fastapi/main.py

import os
import uuid
import shutil
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Header
from fastapi.staticfiles import StaticFiles

from dotenv import load_dotenv
load_dotenv(".env.local")


app = FastAPI()

# mount uploads at /files
app.mount("/files", StaticFiles(directory="uploads"), name="uploads")

API_KEY = os.getenv("FASTAPI_API_KEY")  # loaded from .env
DATABASE_URL = os.getenv("DATABASE_URL")  

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return True

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    _: bool = Depends(verify_api_key),
):
    ext      = Path(file.filename).suffix
    filename = f"{uuid.uuid4().hex}{ext}"
    dest     = Path("uploads") / filename

    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": filename, "url": f"/files/{filename}"}
