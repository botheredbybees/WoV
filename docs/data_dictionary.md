### 📘 Data Dictionary — Nuyina Wildlife Observation System

📅 Last updated: August 2025
🌐 Scope version: **v0.3.0**
🧭 Purpose: Defines all database tables and key fields used in the project's core schema, covering taxonomic, observational, and reference data.

---

### 🐾 1. Table: `wov_dictionary`

**Description**: Metadata for interpreting column names, units, standards, instruments, and CSV definitions. Used internally for automation and export consistency.

| Field | Type | Description |
| :--- | :--- | :--- |
| `dictionary_id` | integer | Primary key |
| `parameter_or_variable` | text | Shorthand used in schemas or CSVs |
| `definition` | text | Human-readable explanation |
| `units` | text | Physical or derived units |
| `sampling_instrument`| text | Tool used to collect this data |
| `standard` | text | Source standard (Darwin Core, ISO, etc.) |
| `csv_files` | text | Used for tracing to inputs/exports |

---

### 🐳 2. Table: `wov_inaturalist_taxa`

**Description**: Imported external taxa matched to iNaturalist. Canonical scientific taxonomy reference used for reconciliation and export.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | integer | Unique row ID (internal) |
| `inaturalist_taxa_id`| integer | iNat taxon identifier (unique) |
| `taxonid` | varchar | LSID or DOI-formatted taxon reference ID |
| `identifier` | varchar | Identifier |
| `parentnameusageid` | varchar | Parent name usage ID |
| `kingdom` | varchar | Kingdom |
| `phylum` | varchar | Phylum |
| `class` | varchar | Class |
| `order` | varchar | Order |
| `family` | varchar | Family |
| `genus` | varchar | Genus |
| `specificepithet` | varchar | Specific epithet |
| `infraspecificepithet` | varchar | Infraspecific epithet |
| `modified` | varchar | Modified date |
| `scientificname` | varchar | Scientific name |
| `taxonrank` | varchar | Taxon rank (species, family, genus, etc.) |
| `reference_url` | varchar | Original source or LSID |

**Indexes**:
- `idx_scientificname`
- `idx_taxa_id`

---

### 🦑 3. Table: `wov_taxa`

**Description**: Local comprehensive taxonomy reference including matched names, classification, origin source data, citation, image links and more.

| Field | Type | Description |
| :--- | :--- | :--- |
| `taxa_id` | integer | Primary key |
| `original_name` | text | Name as initially entered or detected |
| `matched_canonical` | text | Normalized canonical match |
| `matched_name` | text | Canonical match (user-facing) |
| `source_key` | text | LSID, DOI, or DB reference ID |
| `current_name` | text | Source-standard scientific name |
| `current_canonical` | text | Normalized current name |
| `synonym` | text | Is this a synonym of the matched name? |
| `data_source_id` | text | Unique source identifier (e.g., GBIF ID) |
| `data_source_title` | text | Authority system (e.g., "WoRMS", "GBIF") |
| `current_classification_path` | text | Full classification path |
| `joined_name` | text | Joined name |
| `source` | text | Source |
| `level` | text | Taxonomic level |
| `current_base_name` | text | Current base name |
| `current_source` | text | Current source |
| `taxonomy_kingdom` to `taxonomy_genus` | text | Taxonomic classification path |
| `citation` | text | Citable reference for this row |
| `description` | text | Species/Taxon description |
| `wikipedia_url` | text | Link to canonical public species reference |
| `inaturalist_taxa_id` | integer | FK to `wov_inaturalist_taxa.id` |

---

### 📸 4. Table: `wov_inaturalist_observations`

**Description**: Individual records either imported from or exported to iNaturalist. Includes geolocation, timestamps, taxon links, attribution, and observer metadata.

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | integer | Observation ID (iNat) |
| `observed_on_string` | text | String representation of observed on date |
| `observed_on`, `time_observed_at` | date, timestamp | Local or EXIF-parsed timestamp |
| `time_zone` | text | Time zone of observation |
| `user_id`, `user_login`, `user_name` | integer, text, text | Observer or uploader information |
| `created_at`, `updated_at` | timestamp | Timestamps for creation and last update |
| `quality_grade` | text | Research, casual, or needs ID |
| `license` | text | Attribution and media |
| `url` | text | URL of the observation |
| `image_url`, `sound_url` | text | URLs for image and sound files |
| `tag_list` | text | Tags associated with the observation |
| `description` | text | Freeform observation notes |
| `num_identification_agreements`| integer | Number of agreements on the identification |
| `num_identification_disagreements`| integer | Number of disagreements on the identification |
| `captive_cultivated` | boolean | Flag for captive or cultivated organisms |
| `oauth_application_id` | integer | ID of the OAuth application used |
| `place_guess` | text | Guess of the observation location |
| `latitude`, `longitude` | float | Decimal lat/lon |
| `positional_accuracy` | integer | Expected error in meters |
| `private_place_guess` | text | Private guess of the observation location |
| `private_latitude`, `private_longitude` | float | Private decimal lat/lon |
| `public_positional_accuracy`| integer | Public positional accuracy |
| `geoprivacy`, `taxon_geoprivacy` | text | Geoprivacy settings |
| `coordinates_obscured` | boolean | Geoprivacy flag |
| `positioning_method`, `positioning_device` | text | Method and device for positioning |
| `species_guess`, `common_name`, `scientific_name` | text | Observation-level species names |
| `iconic_taxon_name` | text | Iconic taxon name |
| `taxon_id` | integer | Foreign key to `wov_inaturalist_taxa` |
| `wov_taxa_id` | integer | Foreign key to local normalized taxa |
| `taxon_kingdom_name` to `taxon_species_name` | text | Taxonomic classification path |

**Relationships**:
- ↔️ `taxon_id` → `wov_inaturalist_taxa.inaturalist_taxa_id`
- ↔️ `wov_taxa_id` → `wov_taxa.taxa_id`

---

### 📢 5. Table: `wov_observations`

**Description**: The core table for storing shipboard-only sightings and associated data. This table is central to the local, offline-first workflow.

| Field | Type | Description |
| :--- | :--- | :--- |
| `observation_id` | integer | Primary key for this observation |
| `inaturalist_observation_id` | integer | External iNaturalist observation ID if applicable |
| `observed_on` | date | Date of observation |
| `time_observed_at` | timestamp | Timestamp of observation |
| `user_id` | uuid | FK to `wov_users.user_id` |
| `user_login` | text | User's login name |
| `species_guess` | text | Species name guessed by observer |
| `common_name` | text | Common name of species |
| `scientific_name` | text | Scientific name of species |
| `latitude`, `longitude` | float | Geospatial coordinates |
| `positional_accuracy` | integer | Accuracy of coordinates in meters |
| `wov_taxa_id` | integer | FK to `wov_taxa` |
| `taxon_id` | integer | FK to `wov_inaturalist_taxa` |
| `license` | text | Licensing information |
| `quality_grade` | text | Data quality grade |
| `description` | text | Description of the observation |
| `coordinates_obscured` | boolean | Indicates if coordinates are obscured |
| `voyage_id` | char(10) | FK to `wov_voyages` |
| `sea_surface_temp` | float | Sea surface temperature from sensor data |
| `wind_speed_true` | float | Wind speed from sensor data |
| `wind_direction_true` | float | Wind direction from sensor data |
| `air_temp` | float | Air temperature from sensor data |
| `salinity` | float | Salinity from sensor data |
| `distance_to_animals` | float | Estimated distance to animals |
| `group_size_estimate` | integer | Estimated group size of animals |
| `vessel_speed` | float | Vessel speed from sensor data |
| `vessel_course` | float | Vessel course from sensor data |

---

### 👥 6. Table: `wov_users`

**Description**: Local user accounts for on-ship sign-on, merged with Supabase Auth ID.

| Field | Type | Description |
| :--- | :--- | :--- |
| `user_id` | uuid | Supabase user UUID (`auth.users.id`) |
| `username` | text | Display name |
| `role` | text | 'scientist' \| 'crew' \| 'admin' |
| `email` | text | Optional onboard contact |
| `created_at` | timestamp | Time of account creation |
| `inaturalist_id` | integer | iNaturalist user ID |
| `upload_to_inaturalist` | boolean | iNaturalist upload preference |
| `upload_to_ebird` | boolean | eBird upload preference |

---

### 🚢 7. Table: `wov_voyages`

**Description**: Organizational table linking observations and trip context.

| Field | Type | Description |
| :--- | :--- | :--- |
| `voyage_id` | char(10) | Primary key |
| `name` | text | Optional descriptive label |
| `start_date` | date | Departure |
| `end_date` | date | Return date |
| `region` | text | Intended ecological region |
| `notes` | text | Optional route/log info |

Used in UI for filtering, dashboards and reports.

---

### 🖼️ 8. Table: `wov_images`

**Description**: Local photo metadata from observations (especially for structured/transect photo uploads).

| Field | Type | Description |
| :--- | :--- | :--- |
| `image_id` | uuid | Auto-generated ID |
| `observation_id` | int | FK to `wov_observations.observation_id` |
| `file_path` | text | Local path or Supabase Storage URL |
| `camera_model` | text | EXIF derived |
| `datetime_original` | timestamp | From EXIF during upload |
| `license` | text | Optional licensing information |

---

### 🔄 Relationships Summary

wov_observations
├──> wov_taxa
│ └──> wov_inaturalist_taxa
├──> wov_users
├──> wov_voyages
└──> wov_images

wov_inaturalist_observations
├──> wov_taxa
└──> wov_inaturalist_taxa

wov_dictionary → supports form + export metadata

---

### 📎 Notes

- **Indexing**: All taxon tables benefit from indexes on canonical names and `inaturalist_taxa_id`.
- **Storage & External References**: URL, citation, and license data are first-class citizens for attribution compliance.
- **Voyage support**: Logs and observations are grouped under 10-char voyage codes (e.g. `V25SUMSEA01`).