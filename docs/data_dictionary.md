# 📘 Data Dictionary — Nuyina Wildlife Observation System

📅 Last updated: August 2025  
🌐 Scope version: v0.2.0  
🧭 Purpose: Defines all database tables and key fields used in the project's core schema, covering taxonomic, observational, and reference data.

---

## 🐾 1. Table: `elog.wov_dictionary`

**Description**: Metadata for interpreting column names, units, standards, instruments, and CSV definitions. Used internally for automation and export consistency.

| Field                 | Type    | Description                                    |
|----------------------|---------|------------------------------------------------|
| `dictionary_id`      | integer | Primary key                                   |
| `parameter_or_variable` | text | Shorthand used in schemas or CSVs             |
| `definition`         | text    | Human-readable explanation                     |
| `units`              | text    | Physical or derived units                      |
| `sampling_instrument`| text    | Sensor or method used                          |
| `standard`           | text    | Source standard (Darwin Core, ISO, etc.)       |
| `csv_files`          | text    | Example source/input files                     |

---

## 🐳 2. Table: `elog.wov_inaturalist_taxa`

**Description**: Imported external taxa matched to iNaturalist. Canonical scientific taxonomy reference used for reconciliation and export.

| Field                | Type        | Description                                   |
|---------------------|-------------|-----------------------------------------------|
| `id`                | integer     | Unique row ID (internal)                      |
| `inaturalist_taxa_id`| integer     | iNat taxon identifier                         |
| `scientificname`    | varchar     | Scientific name                               |
| `genus` to `kingdom`| varchar     | Full taxonomic path                           |
| `references`        | varchar     | Original source or LSID                       |
| `taxonrank`         | varchar     | Taxon rank (species, family, genus, etc.)     |
| `taxonid`           | varchar     | LSID or DOI-formatted taxon reference ID      |

**Indexes**:  
- `idx_scientificname`  
- `idx_taxa_id`  

---

## 🦑 3. Table: `elog.wov_taxa`

**Description**: Local comprehensive taxonomy reference including matched names, classification, origin source data, citation, image links and more.

| Field                    | Type     | Description                                               |
|--------------------------|----------|-----------------------------------------------------------|
| `taxa_id`                | integer  | Primary key                                               |
| `original_name`          | text     | Name as initially entered or detected                     |
| `matched_name`           | text     | Canonical match (user-facing)                             |
| `matched_canonical`      | text     | Normalized canonical match                                |
| `inaturalist_taxa_id`    | integer  | FK to `wov_inaturalist_taxa.inaturalist_taxa_id`          |
| `taxonomy_kingdom` to `taxonomy_genus` | text | Taxonomic classification path             |
| `source_key`             | text     | LSID, DOI, or DB reference ID                              |
| `data_source_id`         | text     | Unique source identifier (e.g., GBIF ID)                  |
| `data_source_title`      | text     | Authority system (e.g., "WoRMS", "GBIF")                  |
| `current_name`           | text     | Source-standard scientific name                           |
| `synonym`                | text     | Is this a synonym of the matched name?                    |
| `description`            | text     | Species/Taxon description                                 |
| `citation`               | text     | Citable reference for this row                            |
| `wikipedia_url`          | text     | Link to canonical public species reference                |

---

## 📸 4. Table: `elog.wov_inaturalist_observations`

**Description**: Individual records either imported from or exported to iNaturalist. Includes geolocation, timestamps, taxon links, attribution, and observer metadata.

| Field                       | Type        | Description                                           |
|----------------------------|-------------|-------------------------------------------------------|
| `id`                       | integer     | Observation ID (iNat)                                |
| `observed_on`, `time_observed_at` | date, timestamp | Local or EXIF-parsed timestamp              |
| `user_id`, `user_login`    | integer, text | Observer or uploader information                    |
| `species_guess`, `common_name`, `scientific_name` | text | Observation-level species names         |
| `latitude`, `longitude`    | float        | Decimal lat/lon                                      |
| `positional_accuracy`      | integer      | Expected error in meters                             |
| `wov_taxa_id`              | integer      | FK to local normalized taxa                          |
| `taxon_id`                 | integer      | FK to iNaturalist taxa                               |
| `image_url`, `license`     | text         | Attribution and media                                |
| `quality_grade`            | text         | Research, casual, or needs ID                        |
| `description`              | text         | Freeform observation notes                           |
| `coordinates_obscured`     | boolean      | Geoprivacy flag                                      |
| `voyage_id`                | char(10)     | FK to future `wov_voyages.voyage_id`                 |

**Relationships**:
- ↔️ `taxon_id` → `wov_inaturalist_taxa.inaturalist_taxa_id`
- ↔️ `wov_taxa_id` → `wov_taxa.taxa_id`  

---

## 👥 5. Table: `elog.wov_users` (Planned)

**Description**: Local user accounts for on-ship sign-on, merged with Supabase Auth ID.

| Field          | Type      | Description                               |
|----------------|-----------|-------------------------------------------|
| `user_id`      | uuid      | Supabase user UUID (`auth.users.id`)     |
| `username`     | text      | Display name                             |
| `role`         | text      | 'scientist' \| 'crew' \| 'admin'         |
| `email`        | text      | Optional onboard contact                 |
| `created_at`   | timestamp | Time of account creation                 |

---

## 🚢 6. Table: `elog.wov_voyages` (Planned)

**Description**: Organizational table linking observations and trip context.

| Field          | Type       | Description                        |
|----------------|------------|------------------------------------|
| `voyage_id`    | char(10)   | Primary key                        |
| `name`         | text       | Optional descriptive label         |
| `start_date`   | date       | Departure                          |
| `end_date`     | date       | Return date                        |
| `region`       | text       | Intended ecological region         |
| `notes`        | text       | Optional route/log info            |

Used in UI for filtering, dashboards and reports.

---

## 🖼️ 7. Table: `elog.wov_images` (Planned)

**Description**: Local photo metadata from observations (especially for structured/transect photo uploads).

| Field          | Type       | Description                              |
|----------------|------------|------------------------------------------|
| `image_id`     | uuid       | Auto-generated ID                        |
| `observation_id` | int      | FK to `wov_inaturalist_observations.id` |
| `file_path`    | text       | Local path or Supabase Storage URL       |
| `camera_model` | text       | EXIF derived                             |
| `datetime_original` | timestamp | From EXIF during upload             |
| `license`      | text       | Optional licensing information           |

---

## 🔄 Relationships Summary

wov_observations
├──> wov_taxa
│ └──> wov_inaturalist_taxa
├──> wov_users
├──> wov_voyages
└──> wov_images (planned)

wov_dictionary → supports form + export metadata


---

## 📎 Notes

- **Indexing**: All taxon tables benefit from indexes on canonical names and `inaturalist_taxa_id`.
- **Storage & External References**: URL, citation, and license data are first-class citizens for attribution compliance.
- **Voyage support**: Logs and observations are grouped under 10-char voyage codes (e.g. `V25SUMSEA01`).

---



