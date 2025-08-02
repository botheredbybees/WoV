## Functional Design

### 1. Observation Workflow

- **Log an Observation**
  - Simple “New Observation” form: Species (or unidentified), number observed, behavior, notes, distance/bearing from ship (if known), GPS (from camera sensor or manual entry), observer
  - Attach photo(s): Direct from device camera, or file upload

- **Automated Context Injection**
  - Retrieve environmental parameters (location, weather, sensor data) at timestamp of observation via API
  - For photo uploads, extract EXIF datetime and match with nearest sensor data

- **Community View**
  - Voyage-wide summary dashboard
  - Dashboards (“species counts”, “rare sightings”,”voyage faves” etc.)
  - Observation review/verification queue for scientist/crew-led checks
  - Daily summary/evening review board

- **Species Identification**
  - Quick access to locally cached images from Antarctic species databases (AADC) and iNaturalist
  - Optionally, run local AI inference for species suggestions on uploaded images when resources permit

- **Data Management**
  - All observation, photo, and context data stored in local PostgreSQL
  - Export utility for iNaturalist-compliant CSV or API payloads
  - Admin interface for managing species lists, system status, and data export

### 2. Technical Stack Suggestions

- **Frontend:** Responsive web application (e.g., SvelteKit, Vue)
- **Backend:** Node.js/Python/FastAPI/Flask server mediating between frontend, PostgreSQL, and underway data API (influxDB)
- **Database:** Local PostgreSQL (leveraging existing systems)
- **Integration:** API client for ship sensor data; scripts for EXIF extraction; batch photo uploader
- **Optional:** Local microservice for ML/AI identification using downloaded iNaturalist models

### 3. User Roles

- **General User (Crew/Scientist):** Log observations, upload photos, browse voyage summary, view species guide
- **Admin/Lead Scientist:** Manage data, validate/verify records, export datasets, maintain species lists

### 4. Data Flow

1. **Observation Entry:** User enters data manually, or uploads photo (from device or pro camera)
2. **Context Fetch:** System pulls environmental parameters from underway API using time (or EXIF timestamp)
3. **Local Storage:** All info (observation, sensor data, photo) saved to on-ship PostgreSQL
4. **Community Display:** Aggregate visualizations and summaries for shipboard morale and engagement
5. **Export:** On demand, batch output for sharing with AADC/iNaturalist or for post-voyage synthesis