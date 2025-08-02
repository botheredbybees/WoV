
## 📊 Data Design Document: Nuyina Wildlife Observation System

📅 Drafted: August 2025  
📦 Schema Version: 0.2.0  
👤 Author: Platform development team (WoV project)

### 📘 Purpose

This document defines and documents the current and proposed database schema used within the Nuyina Wildlife Observation System (WoV). It is intended to guide ongoing development of:

- Onboard data collection (structured + casual)
- Taxonomic reconciliation
- Attribution and licensing
- Export support (iNaturalist, ALA, eBird)
- Sensor-context integration
- Offline resilience onboard RSV Nuyina

## 📐 Entity Definitions (Current)

### 1. `elog.wov_dictionary`

A central parameter dictionary for recorded variables (e.g. survey metadata, instrument types, data descriptors).

| Field                  | Description                             |
|------------------------|-----------------------------------------|
| `dictionary_id`        | Primary key                             |
| `parameter_or_variable`| Name used in field input or csv         |
| `definition`           | Meaning or contextual explanation       |
| `units`                | Measurement units                       |
| `sampling_instrument` | Tool used to collect this data          |
| `standard`             | Format or guideline used (e.g. Darwin Core) |
| `csv_files`            | Used for tracing to inputs/exports      |

🔎 Used internally for future automated mapping, validation or standardization.

### 2. `elog.wov_inaturalist_taxa`

Imported taxonomic metadata modelled on iNaturalist’s hierarchy and field conventions.

| Field            | Description                                           |
|------------------|-------------------------------------------------------|
| `id`             | Local primary key                                     |
| `inaturalist_taxa_id` | Unique iNat taxon ID                            |
| `scientificname`, `genus`... | Full taxonomic breakdown                  |
| `references`, `modified`     | Metadata support                          |

🔗 Connected via FK to `wov_inaturalist_observations`.

### 3. `elog.wov_taxa`

Locally resolved taxa from submitted observations, possibly matched via various external tools (e.g. GBIF, CoL).

| Field              | Description                                         |
|--------------------|-----------------------------------------------------|
| `taxa_id`          | Local ID — PK                                       |
| `original_name`    | Entered by observer                                 |
| `matched_name`     | System match                                        |
| `synonym`, `source_key`, `data_source_id` | Resolution tracking           |
| `taxonomy_*` fields| Classifications                                    |
| `inaturalist_taxa_id` | Optional link (FK) if reconciled                 |

🧠 Supports flexible resolution/workflow-based ID refinement.

### 4. `elog.wov_inaturalist_observations`

Observations imported from the iNat API or exported by users to iNat.

| Field                    | Description                                      |
|--------------------------|--------------------------------------------------|
| `id`                     | Remote ID (iNat assigned)                        |
| `observed_on`, `time_observed_at` | Local and ISO datetime                 |
| `user_id`, `user_login`, `user_name` | Author identifiers (possibly linked)|
| `taxon_id`, `wov_taxa_id` | Links to iNat and WoV taxonomic tables         |
| `latitude`, `longitude`, `accuracy` | Geospatial fields                   |
| `image_url`, `description`, `quality_grade` | Rich metadata from iNat      |
| `license`                | Licensing info                                  |

🌐 Backbone of outbound sync/export with attribution.

## 🔧 Proposed Additions

### 5. `elog.wov_users`

Tracks users locally — shipboard accounts, authentication metadata, contributor roles.

| Field              | Description                          |
|--------------------|--------------------------------------|
| `user_id`          | Local unique identifier              |
| `username`         | Display name                         |
| `email`            | Optional (for verification/logging)  |
| `sub`              | Supabase Auth ID or JWT sub claim    |
| `role`             | 'observer' \| 'scientist' \| 'admin' |
| `created_at`       | Timestamp of signup                  |

🔑 Required for crew/scientist-led access control and export traceability. Integrates with Supabase Auth (GoTrue).

### 6. Add `voyage_id` to `wov_inaturalist_observations`

```sql
ALTER TABLE elog.wov_inaturalist_observations
ADD COLUMN voyage_id CHAR(10);
```

Rationale:

- Ties observations to a specific voyage log (essential for context, summaries, delay-tolerant export setup).
- Can be further normalized later with a `voyages` table.

### 7. Proposed: `elog.wov_voyages`

Manage voyage metadata, dates, ship, route, and configuration.

| Field        | Description                                 |
|--------------|---------------------------------------------|
| `voyage_id`  | 10-character human-meaningful code (PK)     |
| `name`       | Optional long name e.g. "2025 Season 3"     |
| `start_date` | Voyage commencement                         |
| `end_date`   | Return date or expected end                |
| `region`     | Southern Ocean, Heard Island, etc.         |
| `notes`      | Optional freeform/log tracking             |

📎 Cross-linked to all related data (observations, summaries, sensor logs, exports).

### 8. Proposed: `elog.wov_images`

Structured table for managing multiple observer-submitted images.

| Field            | Description                                 |
|------------------|---------------------------------------------|
| `image_id`       | Primary key                                 |
| `observation_id` | FK to `wov_inaturalist_observations.id` or shipboard log |
| `filename`       | Base name or stored UUID                   |
| `path`           | Filesystem path or Supabase storage key    |
| `uploaded_at`    | Timestamp                                   |
| `camera_model`   | From EXIF                                   |
| `datetime_original` | From EXIF                               |

📸 Helps link professional images back to observations with full metadata, including spatial accuracy.

## 🔄 Relationships Summary

```text
wov_observations
  |
  |-- image(s) —> wov_images
  |
  |-- taxon —> wov_taxa —> wov_inaturalist_taxa
  |
  |-- user —> wov_users
  |
  |-- voyage —> wov_voyages

wov_dictionary: standalone metadata lookup table
```

## ✨ Future Extensions

| Table                | Purpose                                      |
|----------------------|----------------------------------------------|
| `elog.wov_sightings` | Shipboard-only sightings (offline form input) |
| `elog.wov_exports`   | Tracks what/when/where data was exported     |
| `elog.wov_sensor_context` | Snapshot of underway data assoc. per obs |
| `elog.wov_species_list` | Voyage-specific watchlists, e.g. seabirds |

## 🧾 Licensing and Attribution Notes

- Attribution metadata will be stored per observation/photo in `license`, `user_id`, `user_login`.
- Export-layer formatting rules (Darwin Core, iNat CSV, eBird checklists) are designed as external templates and can map back to the tables described here.
- Sensitive fields (e.g., `private_latitude`, `geoprivacy`) are retained but removed during open-data exports.

## ✅ Next Steps

- Normalize user table (`wov_users`) structure and integrate with Supabase Auth (`sub` field).
- Add `voyage_id` to relevant observation and log tables.
- Develop migration + init SQL scripts for `wov_voyages` and `wov_images`.
- Define observation input schema for local web client (Form structure ↔ backend models).
- Add JSON export views aligned with iNat/ALA schema.

Would you like:

- example ER diagram sketches?
- PostgREST views draft?
- Named views for Darwin Core mapping?



## ✅ Purpose of `elog.wov_taxa`

This table serves as the **primary local taxonomy reference** to:

- Normalize species names entered by users.
- Record original, matched, and current taxon names.
- Track taxonomic hierarchy and provenance (GBIF, WoRMS, NZOR, etc.).
- Link with external systems such as iNaturalist, ALA, and your own species dictionary.
- Preserve synonyms and classification history for use in CSV export or UI display.

## 🧠 Key Observations from Current Data

| Column                    | Notes |
|--------------------------|-------|
| `original_name`, `matched_name`, `matched_canonical` | Preserves fuzzy-matched or verified names. Helpful for displaying both what was recorded and what was resolved. |
| `source_key`, `data_source_id`, `data_source_title` | Useful for backtracking source of taxonomy. 👍 |
| `current_name`, `current_classification_path` | Good summary structure for classification mapping. |
| `inaturalist_taxa_id` | Enables joins with iNaturalist taxon metadata table. |
| `taxonomy_` fields | These denormalized fields make it easy to access taxonomic rank in UI and exports. |
| `description`, `wikipedia_url`, `citation` | Ideal for scientific context and user-facing guidance. |

## 🧩 Integration Recommendations

### 1. Indexing

You already have useful indexes on:
- `matched_canonical`
- `inaturalist_taxa_id`

You may also want to add:

```sql
CREATE INDEX idx_current_name ON elog.wov_taxa(current_name);
CREATE INDEX idx_original_name ON elog.wov_taxa(original_name);
```

To optimize fuzzy lookups from form inputs.

### 2. Use Cases This Supports

| Feature/Workflow                                     | Supported by `wov_taxa`? |
|------------------------------------------------------|---------------------------|
| Data entry validation / correction                   | ✅ via `matched_canonical` logic |
| Taxon-based photo galleries                          | ✅ via `taxonomy_class`, `genus`, etc. |
| Darwin Core export                                   | ✅ ~ almost ready-to-go |
| iNaturalist export                                   | ✅ via `inaturalist_taxa_id` |
| ALA species guides                                   | ✅ (matches your export templates folder) |
| Linking to field-guide images                        | ✅ if `joined_name`/canonical is stable |

## 🧱 Additional Feature Suggestions

### 🗃️ Add table: `elog.wov_taxon_sources`

Track authority sources in a normalized way instead of repeating strings like "WoRMS" or "GBIF".

| Field             | Description                     |
|------------------|---------------------------------|
| `source_id`       | e.g. `9`, `11`                  |
| `title`           | e.g. `GBIF Backbone Taxonomy`   |
| `full_url`        | e.g. DOI or homepage            |
| `last_updated`    | Timestamp from last refresh     |

Could be joined to from `wov_taxa.data_source_id`.

### 🌿 Add table: `wov_species_guides` (optional)

Link taxa to onboard image guides, structured by voyage or region.

| Field       | Description                              |
|-------------|------------------------------------------|
| `guide_id`  | Primary key                              |
| `taxa_id`   | FK to `wov_taxa`                         |
| `image_path`| Path or object key in Supabase storage   |
| `context`   | Text or JSON explaining usage            |

## ✅ This Table Is “Export Ready”

For e.g., Darwin Core format, you'll likely only need to:

- Map your fields to Darwin Core terms in a view or function.
- Filter by voyage or export flag.

This will work especially well once `wov_inaturalist_observations.voyage_id` is implemented as discussed earlier.

Let me know if you'd like:

- A suggested SQL view that translates `wov_taxa` + obs into iNaturalist export format?
- A visual ERD showing relations between `wov_taxa`, `inaturalist_observations`, and others?
- A data dictionary in Markdown for your `/docs` folder?

Happy to generate any of those.

Citations:
[1] docker-compose.yml https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/3871842/fb6ca245-09fc-4e29-9f88-7c3e53ac3373/docker-compose.yml
