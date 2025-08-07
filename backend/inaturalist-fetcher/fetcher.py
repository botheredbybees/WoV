import os
import time
import requests
import psycopg2
from psycopg2.extras import DictCursor
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv(".env.local")

# --- Environment Variables ---
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = "db"
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SERVICE_ROLE_KEY")
SUPABASE_BUCKET = "photo-uploads"

# --- Supabase Client ---
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST
    )

def fetch_observations_without_images():
    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute("""
                SELECT obs.observation_id, obs.inaturalist_observation_id
                FROM wov.wov_observations obs
                LEFT JOIN wov.wov_images img ON obs.observation_id = img.observation_id
                WHERE obs.inaturalist_observation_id IS NOT NULL AND img.image_id IS NULL;
            """)
            return cursor.fetchall()

def get_inaturalist_image_url(observation_id):
    url = f"https://api.inaturalist.org/v1/observations/{observation_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["results"] and data["results"][0]["photos"]:
            return data["results"][0]["photos"][0]["url"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from iNaturalist API: {e}")
    return None

def upload_image_to_supabase(image_url, observation_id):
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        file_extension = os.path.splitext(image_url.split('?')[0])[-1] or '.jpg'
        file_name = f"{observation_id}_{int(time.time())}{file_extension}"

        supabase.storage.from_(SUPABASE_BUCKET).upload(
            file_name, response.content
        )
        return file_name
    except (requests.exceptions.RequestException, Exception) as e:
        print(f"Error uploading image to Supabase: {e}")
    return None

def save_image_reference(observation_id, file_path):
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO wov.wov_images (observation_id, file_path)
                VALUES (%s, %s);
            """, (observation_id, file_path))
            conn.commit()

def main():
    print("--- iNaturalist Image Fetcher Started ---")
    while True:
        observations = fetch_observations_without_images()
        if observations:
            print(f"Found {len(observations)} observations without images.")
            for obs in observations:
                print(f"Processing observation ID: {obs['observation_id']}")
                image_url = get_inaturalist_image_url(obs['inaturalist_observation_id'])
                if image_url:
                    print(f"  Found image URL: {image_url}")
                    file_path = upload_image_to_supabase(image_url, obs['observation_id'])
                    if file_path:
                        print(f"  Uploaded to Supabase at: {file_path}")
                        save_image_reference(obs['observation_id'], file_path)
                        print("  Saved image reference to database.")
        else:
            print("No new observations to process. Waiting...")

        time.sleep(60) # Wait for 60 seconds before checking again

if __name__ == "__main__":
    main()
