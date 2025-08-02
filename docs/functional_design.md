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

- **Frontend:** SvelteKit (or Vue, etc.)
  - Connects directly to **Supabase REST API** endpoints (via PostgREST)
  - Uses **Supabase Auth** (GoTrue) via Kong for seamless login/roles
  - Handles most CRUD via auto-generated API

- **Supabase Core Services:**
  - **supabase-db:** Local PostgreSQL data with full schema
  - **supabase-kong:** API gateway for REST, Storage, and Auth
  - **supabase-rest:** PostgREST for auto CRUD/view endpoints
  - **supabase-auth:** GoTrue Auth (Sign-up, login, roles/JWT)
  - **supabase-storage:** Native file/photo upload and management (with webhook support)
  - **supabase-imgproxy:** Fast, compatible image resizing and preview

- **Docker Python `exif-batcher` service:**
  - Receives photo-upload events via webhook (from Supabase Storage through Kong)
  - Downloads images from Supabase Storage bucket
  - Extracts EXIF data (timestamp, GPS) and finds nearest matching sensor/environmental data (from underway table or API)
  - Updates relevant observations in DB (direct or via REST API)
  - Moves/marks files as processed after completion

- **(Optional:) FastAPI (or other backend)**:
  - Can be included for advanced custom logic but not required for normal CRUD and file workflows

- **Offline/Resilience:** All components run in Docker Compose; supports full operation without internet while at sea.

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
