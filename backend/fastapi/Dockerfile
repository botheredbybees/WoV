# WoV/backend/fastapi/Dockerfile
# Use a more secure and updated slim Python image based on Debian Bookworm
FROM python:3.11-slim-bookworm

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies needed for psycopg2 (a common PostgreSQL adapter)
# libpq-dev provides the necessary development files for PostgreSQL client libraries.
# gcc is needed to compile some Python packages that have C extensions (like psycopg2).
# --no-install-recommends helps keep the image size down by not installing recommended packages.
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    # Clean up apt caches to reduce image size
    && rm -rf /var/lib/apt/lists/*

# Copy the Python dependency list and install them
# Ensure you have a 'requirements.txt' file in 'backend/fastapi/'
# Using --no-cache-dir reduces the image size by not storing pip's cache.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY . .

# Expose the port that FastAPI will listen on internally
EXPOSE 8000

# Command to run your FastAPI application
# This assumes your main FastAPI app object is named 'app' in 'main.py'
# --host 0.0.0.0 makes the server accessible from outside the container.
# --port 8000 specifies the internal port.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
