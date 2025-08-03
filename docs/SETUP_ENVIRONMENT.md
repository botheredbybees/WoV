# Environment Setup Guide for Nuyina Wildlife Observation System

This document explains how to prepare and configure your local environment for running the minimal Supabase + FastAPI Docker Compose stack.

---

## Prerequisites

Before starting, ensure you have the following installed on your system:

- **Docker (version 20.10+)**  
  Check with:  
docker --version

text
Install instructions: https://docs.docker.com/get-docker/

- **Docker Compose**  
For Ubuntu, you may need to install the Docker Compose plugin:  
sudo apt update
sudo apt install docker-compose-plugin

text
Check version with:  
docker compose version

text
Alternatively, install standalone `docker-compose`:  
sudo apt install docker-compose
docker-compose --version

text

- **Git** (optional, for cloning the repository)  
Check with:  
git --version

text

---

## .env File Configuration

The Docker Compose setup depends on environment variables for database credentials, API secrets, and service configuration. Create a `.env` file in the root of your project directory based on `.env.example`.

### Example `.env.example` content:

PostgreSQL / Supabase Database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=SuperSecretLongPassword
POSTGRES_DB=wildlife
POSTGRES_PORT=5432

JWT secrets
JWT_SECRET=supersecretjwtkeyvaluechangeme
JWT_EXPIRY=3600

PostgREST API settings
PGRST_DB_SCHEMAS=public,storage
PGRST_DB_ANON_ROLE=anon

Supabase Auth/Storage keys (if included)
SITE_URL=http://localhost:3000
ANON_KEY=supersecretanonkeychangeme
SERVICE_ROLE_KEY=supersecretservicerolekeychangeme

Optional: InfluxDB environment variables (if using the influxdb service)
INFLUXDB_ADMIN_USER=admin
INFLUXDB_ADMIN_PASSWORD=adminpassword
INFLUXDB_ORG=nuyina
INFLUXDB_BUCKET=underway

text

**Important:**  
- Replace all placeholder secrets with strong, randomly generated values before deploying or sharing.  
- Never commit your real `.env` file to version control; use `.env.example` as a template only.  
- The `POSTGRES_PORT` variable should be set to `5432` to reflect the internal container port, regardless of host port mapping.

---

## Running the Docker Compose Stack

1. Clone the repository (if you haven't already):

git clone https://github.com/botheredbybees/WoV.git
cd WoV

text

2. Create your `.env` file from `.env.example`:

cp .env.example .env

text

Edit `.env` and update the variables with your actual credentials and secrets.

3. Start the containers in detached mode:

docker-compose up -d

text

or if using the Docker Compose plugin:

docker compose up -d

text

4. Check running containers and health status:

docker-compose ps

text

All services should be running with a `healthy` status after startup.

---

## Accessing Services

- **PostgreSQL Database:**  
Host: `localhost`  
Port: as mapped (often `5433` if configured like in compose)  
User, DB, Password: as set in `.env`

- **PostgREST API:**  
Available at `http://localhost:3003`

- **Supabase Auth (GoTrue):**  
Running at `http://localhost:9999`

- **FastAPI Service:**  
Running at `http://localhost:8000`

---

## 🧭 Setting Up the Frontend (SvelteKit)

To run the field data entry interface, install and launch the SvelteKit frontend:

### Prerequisites

Install the following (in addition to Docker):

- Node.js (v20+ recommended)  
  https://nodejs.org/en/download  
  Test with: `node -v`

- npm or pnpm  
  Test with: `npm -v`  
  Supabase client + SvelteKit is installed via npm packages.

---

### 1. Install and Bootstrap the Frontend

From the project root:

cd frontend
npm install # or: pnpm install


This installs the app dependencies, including:

- SvelteKit
- Supabase JS client
- UI libraries
- Upload helpers

---

### 2. Configure Environment for Frontend

Copy `.env.example` and adjust Supabase and site settings (see above)

---

### 3. Start the Frontend

To run in development mode:

npm run dev



You should now be able to open the field data UI at:

📍 http://localhost:5173

---

### 4. Testing Upload

Log in via Supabase Auth, create a new observation, and try uploading a photo. It should appear in your Supabase bucket and trigger exif-batcher via webhook.

---

### Notes

- This frontend is being developed incrementally. Not all features (offline sync, admin control, ML preview) may be available yet.
- If you're building for iOS/Android field testing, instruct users to connect via local WiFi and the machine's IP rather than localhost.



---

## Troubleshooting Tips

- If you see warnings about missing environment variables, check your `.env` exists and contains all required variables.
- If `docker-compose` or `docker compose` commands are not recognized, verify your Docker and Docker Compose installation and use the appropriate command.
- If images fail to pull with "access denied" errors, ensure image names and tags in `docker-compose.yml` are correct.
- Volumes mounting SQL scripts require those files present in your specified paths (e.g., `./volumes/db/realtime.sql`). Confirm the files exist with proper permissions.

---

## Additional Resources

- Supabase self-hosting with Docker: https://supabase.com/docs/guides/self-hosting/docker  
- Docker official docs: https://docs.docker.com/  
- Docker Compose guide: https://docs.docker.com/compose/  

---

*For further assistance, please open an issue or discussion on the GitHub repository.*