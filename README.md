🐧 Nuyina Wildlife Observation System
📦 Version: 0.3.0
📅 Status: In Planning
🌐 License: Creative Commons Attribution (CC BY 4.0) (recommend revisiting at launch)

🚢 Overview
This project documents the planning and development of a shipboard biodiversity logging platform for the RSV Nuyina.

The system is designed to support:

Casual expeditioner wildlife sightings (e.g., seabirds, whales, seals)

Structured ecological surveys (e.g., pelagic bird transects)

Integration with automated environmental context (via the InfluxDB-based underway data API)

Seamless and license-aware export to iNaturalist, ALA, and other biodiversity platforms

🌟 Key Goals
🖥️ Cross-device web app for logging, reviewing, and exporting onboard wildlife observations.

📶 Offline-first operation with a fully local backend (Docker + Supabase + FastAPI).

📸 Image annotation and EXIF-based data linking for professional photo uploads.

🔁 Modular export support: ALA (Darwin Core), iNaturalist, eBird, BioCollect.

🗳️ Group participation & engagement: voting, summaries, “photo of the voyage.”

🔐 Rich attribution + licensing metadata integrated at all levels.

👥 Audience
Casual users (expeditioner photographers, general crew)

Scientific observers conducting structured protocols

Data management/admin teams

External data consumers: iNaturalist, ALA, AAD

🛠️ Technology Stack
Layer	Tool(s)
Frontend	SvelteKit / Vue 3 (touch & offline-friendly)
Backend	FastAPI (Python), Dockerized
Auth + Storage	Supabase (PostgreSQL, Auth, Storage + Studio)
Sensor Data	InfluxDB (underway data, containerized restore)
Image Viewer	HTML-based, zoomable image reference guide

Export to Sheets
📁 Repository Structure
```
/
├── README.md
├── docs/
│   ├── data_design.md
│   ├── data_dictionary.md
│   ├── data_model_ERD.md
│   ├── environment_setup_guide.md
│   ├── EXIF_batcher.md
│   ├── export-templates/
│   │   ├── iNaturalist_CSV_example.csv
│   │   ├── eBird_checklist_template.csv
│   │   └── ALA_DarwinCore_template.csv
│   ├── functional_design.md
│   ├── project_brief.md
│   └── timeline.md
├── backend/
│   ├── exif-batcher/
│   └── fastapi/
├── supabase/
│   ├── migrations/
│   ├── .branches/
│   └── .temp/
├── data/
│   └── sql/
└── .gitignore
```
Note: The supabase/ directory and its contents are managed automatically by the Supabase CLI and should not be modified manually.

📦 Getting Started
This guide assumes you are starting with a clean repository clone.

Clone the repository:

Bash

git clone https://github.com/botheredbybees/WoV.git
cd WoV
Install Prerequisites for Rocky Linux 8:

Docker Engine & Docker Compose: Follow the official Docker documentation for RHEL to install these.

Node.js & npm: Install via the NodeSource repository on RHEL.

Supabase CLI: Install as a dev dependency using npm.

Bash

npm i supabase --save-dev
Git: Install via sudo dnf install git.

Initialize and start Supabase services: This command will start all the necessary Docker containers for your local Supabase stack and apply your database schema defined in supabase/migrations/.

Bash

npx supabase db reset
Load Initial Data: Load the large SQL data files directly into the running PostgreSQL container using docker exec.

Bash

# First, verify your PostgreSQL container's name, it should be something like supabase_db_WoV
docker ps --filter "ancestor=public.ecr.aws/supabase/postgres" --format "{{.Names}}"

# Then, run the data load commands using the correct container name
docker exec -i <CONTAINER_NAME> psql -U postgres -d postgres < data/sql/01_wov_inaturalist_taxa.sql
docker exec -i <CONTAINER_NAME> psql -U postgres -d postgres < data/sql/02_wov_taxa.sql
docker exec -i <CONTAINER_NAME> psql -U postgres -d postgres < data/sql/03_wov_inaturalist_observations.sql
docker exec -i <CONTAINER_NAME> psql -U postgres -d postgres < data/sql/04_wov_dictionary.sql
docker exec -i <CONTAINER_NAME> psql -U postgres -d postgres < data/sql/05_seed_data.sql
Verify Setup: Check that Supabase Studio is accessible at http://localhost:54323 and that your tables and data are present in the wov schema.

📄 Documentation Index
Project Brief

Functional Design

Data Design

Data Dictionary

Data Model (ERD)

EXIF Batcher Design

Environment Setup Guide

Project Timeline

📤 Export Templates — Coming soon

🤝 Contributions
Planning is collaborative! Feel free to open:

Ideas and enhancements

Structured export examples

Documentation PRs

📝 License & Attribution
Field observations and photos will be optionally released under researcher-chosen licenses (CC-BY / CC0 where possible). The platform's code will be MIT or similar.

Data sharing is designed to comply with ALA and iNaturalist rules around attribution, consent, and licensing.
