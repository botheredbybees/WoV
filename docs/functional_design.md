## Functional Design

### 1. Observation Workflow

- **Log an Observation**
  - Simple “New Observation” form: Species, number observed, behavior, notes, distance/bearing from ship, GPS, observer
  - Photo attachment: from device camera or upload

- **Automated Context Injection**
  - Retrieve contextual parameters (location, weather, sensor data) at time of observation via API
  - For photo uploads, **extract EXIF datetime and location and match with nearest sensor/environmental data**
  - **EXIF/Context batcher**: For bulk or delayed photo uploads, a Dockerized Python service processes new images as they arrive using webhooks or polling. It extracts EXIF data, matches by timestamp to underway sensor data, and updates the observations table. Handles both live and offline/batch operation on the ship.

- **Community View**
  - Voyage/daily summary dashboard, rare sightings, verification, and engagement boards

- **Species Identification**
  - Tied to local taxonomic dictionary and iNaturalist
  - (Optional): Local ML engine for automatic species suggestion

- **Data Management**
  - Observations, photos, and context in PostgreSQL via Supabase
  - Automated and manual export utilities for iNaturalist/ALA/eBird
  - Admin interface for voyage/species/admin operations

### 2. Technical Stack

- **Frontend:** SvelteKit (or Vue, etc.) — talks directly to Supabase/PostgREST, uses Supabase Auth for login
- **Backend:** All CRUD and user management via Supabase (no Python backend required for standard API)
- **Database:** Supabase PostgreSQL
- **Integration:** 
  - API client for ship sensor data
  - **Docker Python “exif-batcher” service** for post-processing and context lookup
  - Scripts/services for batch handling
- **Optional:** Local microservice for AI/ML on images

### 3. User Roles

- **General User (Crew/Scientist):** Log observations, upload/view photos, access summary dashboards/species lists
- **Admin/Lead Scientist:** Review/verify data, export datasets, manage voyage/species dictionaries

### 4. Data Flow

1. **Observation Entry:** Data and image upload via web/UI
2. **Context Fetch:** 
    - **Live:** JS fetches underway/sensor data for instant match
    - **Bulk:** EXIF/Context batcher Python service triggered on upload; updates DB with timestamp and context
3. **Local Storage:** All data integrated in on-ship PostgreSQL
4. **Community Display:** Aggregated visualizations for use onboard
5. **Export:** Batch/scheduled export for ALA, iNat, and eBird integration

### 5. EXIF/Context Docker Batcher

- **Service:** `exif-batcher` (Python)
- **Trigger:** Supabase Webhook on file upload or periodic poll of Storage
- **Process:**
    1. Download new image
    2. Extract EXIF datetime/location
    3. Look up nearest underway/sensor context by time
    4. Update relevant row(s) in observations DB
    5. Mark file as processed or move to archive folder

- **Advantages:**
    - Fits offline/workgroup Docker deployment
    - Resilient to network dropouts and bulk workflows
    - Modular & independently updateable

---

*This design modernizes the stack, enabling low-friction data entry and robust sync to shipboard science workflows without maintaining unnecessary backend code!*
