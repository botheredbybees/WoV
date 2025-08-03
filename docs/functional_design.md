## Functional Design

### 1. Observation Workflow

- **Log an Observation**
  - “New Observation” form: Species, number, behavior, notes, distance/bearing, GPS, observer
  - Attach photo(s): from device camera, upload, SD card, or file drop

- **Automated Context Injection**
  - **EXIF/Context batcher service processes every new image,** live or bulk, by default. Every file upload triggers the batcher via webhook (Supabase Storage via Kong). The batcher:
    1. Downloads the image
    2. Extracts EXIF metadata (datetime, GPS, etc.)
    3. Looks up nearest matching sensor/environment data
    4. Updates/annotates the associated observation in the database (or staging table)
    5. Records processing status or flags for review if EXIF/context fails/missing


- **Community View**
  - Voyage/daily summary dashboard, rare sightings, verification, and engagement boards

- **Species Identification**
  - Tied to local taxonomic dictionary and iNaturalist
  - (Optional): Local ML engine for automatic species suggestion

- **Data Management**
  - Observations, photos, and context stored in Postgres via Supabase
  - Batched, scheduled, and on-demand export for iNaturalist, ALA, and eBird (views + PostgREST)
  - Admin interface for voyage/species/reference data

---

### 2. Technical Stack

- **Frontend:** SvelteKit
  - Communicates directly with Supabase via REST API and Storage client
  - Supports Supabase Auth (login, session, user metadata)
  - Allows offline-first UX with local queuing planned
  - Touch UI = suitable for ship touchscreen, tablet, or laptop interface

- **Backend:** Supabase ecosystem (GoTrue, Storage, PostgREST, Kong)
  - Handles DB, Auth, API, and Storage — no conventional backend server required
  - FastAPI service is optional for custom analytics, ML, or integration logic

- **Database:** Supabase PostgreSQL stack (via Docker)

- **Image and EXIF Context Workflow:**
  - Photos uploaded via frontend
  - Processed by exif-batcher (Docker service)
  - Linked to observations via structured filenames and metadata

- **Optional Add-ons:**
  - Local ML/AI image inference
  - InfluxDB sensor-linking and context matchers
  - Export UI for iNaturalist, ALA, eBird
---

### 3. User Roles

- **General User (Crew/Scientist):** Log observations, upload and review photos, filter voyage/species data, see summary stats
- **Admin/Lead Scientist:** Approve/verify/curate records, manage taxon/voyage lists, export data, keep system healthy

---

### 4. Data Flow

1. **Observation Entry:** Users enter records and upload images through web/mobile app (SvelteKit).
2. **Photo Storage:** Uploaded images stored in Supabase Storage (file bucket).
3. **EXIF/Event Processing:** On upload, Supabase Storage triggers a webhook via Kong to the `exif-batcher` Python service, which extracts and annotates EXIF/context metadata.
4. **Context Fetch:**
    - **Live:** JS fetches underway/sensor data for direct injection
    - **Bulk:** `exif-batcher` service updates DB with EXIF info and nearest context automatically
5. **Database:** All info kept in on-ship PostgreSQL (via Supabase stack)
6. **Community Display:** Visual summaries and aggregation on web/dashboard for voyage engagement, QA, and science
7. **Export:** Export tools/tables/views enable direct ALA, iNaturalist, or eBird submission from local stack

---

### 5. Docker Python EXIF/Context Batcher

- **Service:** `exif-batcher` (Python)
- **Trigger:** Supabase Storage webhook routed via Kong on file upload, or optional poll of the bucket
- **Process:**
    1. Receives event (upload info)
    2. Downloads image from Storage
    3. Reads EXIF fields (datetime, GPS, camera, etc.)
    4. Looks up nearest underway/sensor context by timestamp
    5. Updates associated row in observations or staging DB
    6. Marks the image/job as processed (move or tag)

- **Advantages:**
    - True offline mode (everything in Docker Compose/local network)
    - Handles real-time and batch workflows elegantly
    - Separation of “data entry/UI” and “heavy post-processing” for resilience and speed
    - Modular and simple to update/extend without full-stack rebuild

---

*This design enables fully offline, reliable, and modern marine field data workflows. It leverages Supabase’s strengths for API/auth/storage while preserving extensibility, automation, and performance at sea.*
