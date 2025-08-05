Environment Setup Guide for Nuyina Wildlife Observation System
This document explains how to prepare and configure your local environment for running the full Supabase + FastAPI Docker Compose stack.

Prerequisites
Before starting, ensure you have the following installed on your system:

Docker (version 20.10+)
Check with:

Bash

docker --version
Install instructions: https://docs.docker.com/get-docker/

Docker Compose
For Ubuntu, you may need to install the Docker Compose plugin:

Bash

sudo apt update
sudo apt install docker-compose-plugin
Check version with:

Bash

docker compose version
Alternatively, install standalone docker-compose:

Bash

sudo apt install docker-compose
docker-compose --version
Supabase CLI
This is essential for managing your local Supabase services. Follow the installation instructions for your operating system:
https://supabase.com/docs/guides/local-development

Node.js & npm (for Rocky Linux 8 / RHEL):
The Supabase CLI is a Node.js package, so you must install Node.js and npm first.

Install Node.js from the official NodeSource repository:

Bash

# Replace '18' with the desired Node.js version (e.g., 20).
curl -fsSL https://rpm.nodesource.com/setup_18.x | sudo bash -
sudo dnf install nodejs -y
Verification:

Bash

node --version
npm --version
Git (optional, for cloning the repository):

Installation steps remain the same as previously documented.

Supabase CLI (for Linux)
This is essential for managing your local Supabase services.

Install the Supabase CLI globally using npm:

Bash

npm install -g supabase
Note: If you encounter a permissions error, you may need to use sudo or configure npm's global directory. A common solution is sudo npm install -g supabase --unsafe-perm=true.

Verification:

Bash

supabase --version
Important Note for CLI Version 2.33.9 (or similar):
As observed in development, some versions of the Supabase CLI have been found to not include the supabase sql command in their binary. If supabase --help does not list sql under available commands, you must use the docker exec method for loading SQL data, as detailed in the "Load Initial Data" section. This guide explicitly uses that more robust method.


Git (optional, for cloning the repository)
Check with:

Bash

git --version
Node.js (v20+ recommended)
https://nodejs.org/en/download
Test with: node -v

npm or pnpm (Node Package Manager)
Test with: npm -v
These are used to install JavaScript dependencies for the frontend.

1. Initialize Supabase Project
First, navigate to the root of your project directory (e.g., WoV/ where your docker-compose.yml will eventually reside, or where you cloned the repo).

Initialize the Supabase project:

Bash

supabase init
This command creates a supabase/ directory in your project root, containing essential configuration files and a migrations folder. It also creates a default docker-compose.yml for the core Supabase services.

Create your .env file:
The Supabase CLI typically looks for a .env file in the root of your project. Copy the example and update it.

Bash

cp .env.example .env
Edit .env and fill in the required environment variables. The supabase init command might also generate an example.env for you.
You will need to define at least these secrets for the full Supabase stack:

# Example .env content for full Supabase
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_strong_postgres_password
POSTGRES_DB=postgres # Or your preferred database name, e.g., wildlife
# The following secrets are crucial for Supabase services
# Generate these with `openssl rand -base64 32` for each
SUPABASE_AUTH_JWT_SECRET=supersecretjwtkeyvaluechangeme_generate_new
SUPABASE_DB_JWT_SECRET=anothersupersecretkeyvalue_generate_new
ANON_KEY=supersecretanonkeychangeme_generate_new
SERVICE_ROLE_KEY=supersecretservicerolekeychangeme_generate_new

# Optional: InfluxDB environment variables (if using the influxdb service)
INFLUXDB_ADMIN_USER=admin
INFLUXDB_ADMIN_PASSWORD=adminpassword
INFLUXDB_ORG=nuyina
INFLUXDB_BUCKET=underway
Important:

Replace all placeholder secrets with strong, randomly generated values.

Never commit your real .env file to version control; use .env.example as a template only.

2. Setting Up Initial Database Schema and Data
In a full Supabase setup, schema changes are managed via migrations using the Supabase CLI. Initial data loading can be done via psql or the supabase sql command.

Place Schema Initialization Script as a Migration:
Move your 00_init_schema.sql into the supabase/migrations directory that was created by supabase init. You need to rename it to a timestamped format.

For example, if the current date is August 4, 2025, you could name it:
supabase/migrations/20250804000000_init_wov_schema.sql

This script creates your custom wov schema and its tables. The Supabase CLI will run this after its own core schemas (auth, storage, public) are set up.

Apply Database Migrations:
With your 00_init_schema.sql placed in supabase/migrations, apply it to your database:

Bash

supabase db push
This command will apply any pending migrations, including your wov schema.

Load Initial Data:
Your data files (01_wov_inaturalist_taxa.sql, 02_wov_taxa.sql, 03_wov_observations.sql) are for populating tables, not for defining the schema. You should execute these after the schema has been created by supabase db push.
Place these files in a convenient location (e.g., in a data/sql directory in your project root). Then, use the supabase sql command to load them:

Bash

# Example:
supabase sql -f data/sql/01_wov_inaturalist_taxa.sql
supabase sql -f data/sql/02_wov_taxa.sql
supabase sql -f data/sql/03_wov_observations.sql
Ensure you load them in the correct dependency order as described in your original document (e.g., taxa before observations).

The data/sql directory (or wherever you place them) should now contain:

WoV/
├── supabase/
│   └── migrations/
│       └── <timestamp>_init_wov_schema.sql # Your 00_init_schema.sql, renamed
└── data/
    └── sql/
        ├── 01_wov_inaturalist_taxa.sql
        ├── 02_wov_taxa.sql
        └── 03_wov_observations.sql
3. Running the Docker Compose Stack
The Supabase CLI handles running the full Docker Compose stack for you.

Start all Supabase services locally:

Bash

supabase start
This command will pull necessary Docker images, start all Supabase services (Postgres, Kong, Auth, Storage, Realtime, etc.), and provide you with the local URLs and API keys.

If you need to restart and completely clear your local database, you can use:

Bash

supabase db reset
This will drop and recreate your local database, re-run all migrations, and clear all data. You would then need to re-run your supabase sql commands for initial data.

Check running containers and health status:

Bash

docker compose ps
All services should be running with a healthy status after startup.

🔗 Accessing Local Services
After running supabase start, you can access the various services at the following local URLs:

Supabase Studio (Dashboard): http://localhost:8082

Supabase API Gateway (Kong):

HTTP: http://localhost:8000

HTTPS: https://localhost:8443

Supabase Auth API: http://localhost:8000/auth/v1 (Accessed via Kong)

Supabase REST API (PostgREST): http://localhost:8000/rest/v1 (Accessed via Kong)

Supabase Storage API: http://localhost:8000/storage/v1 (Accessed via Kong)

Your Custom Services (if integrated into supabase/docker/docker-compose.yml or run separately):

Custom FastAPI Service: http://localhost:8004

EXIF Batcher Service: http://localhost:5005 (For direct access/testing; webhooks use internal Docker network names)

Image Proxy Service: http://localhost:5004

4. Setting Up the Frontend (SvelteKit)
To run the field data entry interface, you'll first create the SvelteKit project and then install its dependencies.

Create the SvelteKit Project
First, navigate to the root of your project (e.g., WoV/). Then, use the SvelteKit scaffolding tool to create a new SvelteKit application within a frontend directory.

Bash

cd WoV/
npx sv create frontend
Follow the prompts:

Project name: Enter frontend.

Which SvelteKit project template?: Choose SvelteKit minimal (barebones scaffolding for your new app).

Add type checking with TypeScript?: Select Yes, using TypeScript syntax.

Add ESLint and Prettier for code linting and formatting?: Select both with the spacebar.

Select npm for Which package manager do you want to install dependencies with?

This command will create the WoV/frontend/ directory populated with the basic SvelteKit project structure.

Install Frontend Dependencies
Now, navigate into the newly created frontend directory and install all the project's dependencies. This will install SvelteKit itself and the Supabase JavaScript client library (which will be a dependency of your SvelteKit project if you set up Supabase integration).

Bash

cd frontend
npm install # or: pnpm install if you prefer pnpm
Configure Environment for Frontend
The frontend needs to know about your Supabase project's API URL and anon key to connect to your local Supabase instance. Create a .env file directly inside your frontend directory (i.e., WoV/frontend/.env) and add the following:

VITE_PUBLIC_SUPABASE_URL=http://localhost:8000
VITE_PUBLIC_SUPABASE_ANON_KEY=supersecretanonkeychangeme
Important:

VITE_PUBLIC_SUPABASE_URL should point to the Supabase API Gateway (Kong) HTTP URL, which is http://localhost:8000 by default with supabase start.

VITE_PUBLIC_SUPABASE_ANON_KEY should match the ANON_KEY you set in your main project's .env file (WoV/.env).

These variables are prefixed with VITE_PUBLIC_ because SvelteKit uses Vite, and this prefix makes them accessible in the client-side code.

Start the Frontend
To run the SvelteKit application in development mode, which includes hot-reloading and other developer conveniences:

Bash

npm run dev
You should now be able to open the field data UI at:

📍 http://localhost:5173

5. Testing Upload
Log in via Supabase Auth, create a new observation, and try uploading a photo. It should appear in your Supabase storage bucket and, if configured, trigger exif-batcher via webhook.

Notes
This frontend is being developed incrementally. Not all features (offline sync, admin control, ML preview) may be available yet.

If you're building for iOS/Android field testing, instruct users to connect via local WiFi and the machine's IP rather than localhost.

Troubleshooting Tips
If supabase commands are not recognized, verify your Supabase CLI installation and that it's in your system's PATH.

If supabase start fails, check the output for specific errors. Ensure Docker is running.

If services are not healthy, use docker compose logs <service_name> (e.g., docker compose logs kong) to inspect container logs for errors.

If supabase db push or supabase sql fail, double-check your SQL syntax and file paths.

If images fail to pull with "access denied" errors, ensure image names and tags are correct.

For local development, use supabase stop to gracefully stop services and supabase db reset to clear and re-initialize the database from migrations.

Additional Resources
Supabase self-hosting with Docker: https://supabase.com/docs/guides/self-hosting/docker

Supabase Local Development Guide: https://supabase.com/docs/guides/local-development

Docker official docs: https://docs.docker.com/

Docker Compose guide: https://docs.docker.com/compose/

For further assistance, please open an issue or discussion on the GitHub repository.