import os
import requests
import psycopg2
import logging

# --- Configuration ---
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "wov"
DB_USER = "postgres"
DB_PASSWORD = "SuperSecretLongPassword"
IMAGE_DIR = "inaturalist_images"
MAX_IMAGES_PER_SPECIES = 10

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_db_connection():
    """Establishes a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except psycopg2.OperationalError as e:
        logging.error(f"Database connection failed: {e}")
        return None

def fetch_species(conn):
    """Fetches unique scientific names from the database."""
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT DISTINCT scientific_name FROM elog.wov_inaturalist_observations WHERE scientific_name IS NOT NULL;")
            species = [row[0] for row in cur.fetchall()]
            return species
    except psycopg2.Error as e:
        logging.error(f"Error fetching species from database: {e}")
        return []

def fetch_image_urls(species_name):
    """Fetches image URLs for a given species from the iNaturalist API."""
    urls = []
    try:
        api_url = f"https://api.inaturalist.org/v1/observations"
        params = {
            "taxon_name": species_name,
            "per_page": MAX_IMAGES_PER_SPECIES,
            "quality_grade": "research",
            "photos": "true"
        }
        headers = {
            "User-Agent": "WoV Image Fetcher (Python script)"
        }
        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()

        for result in data.get("results", []):
            if "photos" in result and result["photos"]:
                for photo in result["photos"]:
                    if "url" in photo:
                        # Get a medium-sized image
                        urls.append(photo["url"].replace("square", "medium"))
                        if len(urls) >= MAX_IMAGES_PER_SPECIES:
                            return urls
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed for {species_name}: {e}")
    return urls

def download_image(url, directory, species_name):
    """Downloads an image from a URL and saves it to a directory."""
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Get filename from URL
        filename = os.path.join(directory, url.split("/")[-2] + "_" + url.split("/")[-1])

        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        logging.info(f"Downloaded {filename}")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download {url}: {e}")
        return False

def main():
    """Main function to fetch species and download images."""
    logging.info("Starting image fetching process...")

    # Create main image directory
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    conn = get_db_connection()
    if not conn:
        return

    species_list = fetch_species(conn)
    conn.close()

    if not species_list:
        logging.warning("No species found in the database.")
        return

    logging.info(f"Found {len(species_list)} species to fetch images for.")

    for species in species_list:
        logging.info(f"--- Fetching images for: {species} ---")
        species_dir = os.path.join(IMAGE_DIR, species.replace(" ", "_"))

        image_urls = fetch_image_urls(species)

        if not image_urls:
            logging.warning(f"No images found for {species}")
            continue

        downloaded_count = 0
        for url in image_urls:
            if downloaded_count >= MAX_IMAGES_PER_SPECIES:
                break
            if download_image(url, species_dir, species):
                downloaded_count += 1
        logging.info(f"Downloaded {downloaded_count} images for {species}")

    logging.info("Image fetching process completed.")

if __name__ == "__main__":
    main()
