# backend/fastapi/main.py

import os
import uuid
import shutil
from pathlib import Path
import psycopg2
from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager

from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Header
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
import datetime

from dotenv import load_dotenv
load_dotenv(".env.local")


app = FastAPI()

# Database connection pool
db_pool = SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host="db",
    port="5432",
    database=os.getenv("POSTGRES_DB"),
)

@contextmanager
def get_db_connection():
    conn = db_pool.getconn()
    try:
        yield conn
    finally:
        db_pool.putconn(conn)

@contextmanager
def get_db_cursor(commit=False):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            yield cursor
            if commit:
                conn.commit()
        finally:
            cursor.close()

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

@app.get("/taxa")
async def get_taxa():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM wov.wov_taxa")
        taxa = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in taxa]

@app.get("/voyages")
async def get_voyages():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM wov.wov_voyages")
        voyages = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in voyages]

class Observation(BaseModel):
    inaturalist_observation_id: Optional[int] = None
    observed_on: Optional[datetime.date] = None
    time_observed_at: Optional[datetime.datetime] = None
    user_id: Optional[uuid.UUID] = None
    user_login: Optional[str] = None
    species_guess: Optional[str] = None
    common_name: Optional[str] = None
    scientific_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    positional_accuracy: Optional[int] = None
    wov_taxa_id: Optional[int] = None
    taxon_id: Optional[int] = None
    license: Optional[str] = None
    quality_grade: Optional[str] = None
    description: Optional[str] = None
    coordinates_obscured: Optional[bool] = None
    voyage_id: Optional[str] = None
    sea_surface_temp: Optional[float] = None
    wind_speed_true: Optional[float] = None
    wind_direction_true: Optional[float] = None
    air_temp: Optional[float] = None
    salinity: Optional[float] = None
    distance_to_animals: Optional[float] = None
    group_size_estimate: Optional[int] = None
    vessel_speed: Optional[float] = None
    vessel_course: Optional[float] = None

@app.get("/observations")
async def get_observations():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM wov.wov_observations")
        observations = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in observations]

@app.post("/observations")
async def create_observation(observation: Observation):
    with get_db_cursor(commit=True) as cursor:
        query = """
            INSERT INTO wov.wov_observations (
                inaturalist_observation_id, observed_on, time_observed_at, user_id, user_login,
                species_guess, common_name, scientific_name, latitude, longitude,
                positional_accuracy, wov_taxa_id, taxon_id, license, quality_grade,
                description, coordinates_obscured, voyage_id, sea_surface_temp,
                wind_speed_true, wind_direction_true, air_temp, salinity,
                distance_to_animals, group_size_estimate, vessel_speed, vessel_course
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
            ) RETURNING observation_id;
        """
        cursor.execute(query, (
            observation.inaturalist_observation_id, observation.observed_on,
            observation.time_observed_at, observation.user_id, observation.user_login,
            observation.species_guess, observation.common_name, observation.scientific_name,
            observation.latitude, observation.longitude, observation.positional_accuracy,
            observation.wov_taxa_id, observation.taxon_id, observation.license,
            observation.quality_grade, observation.description, observation.coordinates_obscured,
            observation.voyage_id, observation.sea_surface_temp, observation.wind_speed_true,
            observation.wind_direction_true, observation.air_temp, observation.salinity,
            observation.distance_to_animals, observation.group_size_estimate,
            observation.vessel_speed, observation.vessel_course
        ))
        new_id = cursor.fetchone()[0]
        return {"observation_id": new_id}
