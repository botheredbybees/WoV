can you draft a data design document. here are the tables I already have set up for this project. would you like examples of the data in any of them?
-- Table: elog.wov_dictionary

-- DROP TABLE IF EXISTS elog.wov_dictionary;

CREATE TABLE IF NOT EXISTS elog.wov_dictionary
(
    dictionary_id integer NOT NULL DEFAULT nextval('elog.wov_dictionary_dictionary_id_seq'::regclass),
    parameter_or_variable text COLLATE pg_catalog."default",
    definition text COLLATE pg_catalog."default",
    units text COLLATE pg_catalog."default",
    sampling_instrument text COLLATE pg_catalog."default",
    standard text COLLATE pg_catalog."default",
    csv_files text COLLATE pg_catalog."default",
    CONSTRAINT wov_dictionary_pkey PRIMARY KEY (dictionary_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS elog.wov_dictionary
    OWNER to app_user;
—------------------------------------------------------
-- Table: elog.wov_inaturalist_observations

-- DROP TABLE IF EXISTS elog.wov_inaturalist_observations;

CREATE TABLE IF NOT EXISTS elog.wov_inaturalist_observations
(
    id integer,
    observed_on_string text COLLATE pg_catalog."default",
    observed_on date,
    time_observed_at timestamp without time zone,
    time_zone text COLLATE pg_catalog."default",
    user_id integer,
    user_login text COLLATE pg_catalog."default",
    user_name text COLLATE pg_catalog."default",
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    quality_grade text COLLATE pg_catalog."default",
    license text COLLATE pg_catalog."default",
    url text COLLATE pg_catalog."default",
    image_url text COLLATE pg_catalog."default",
    sound_url text COLLATE pg_catalog."default",
    tag_list text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    num_identification_agreements integer,
    num_identification_disagreements integer,
    captive_cultivated boolean,
    oauth_application_id integer,
    place_guess text COLLATE pg_catalog."default",
    latitude double precision,
    longitude double precision,
    positional_accuracy integer,
    private_place_guess text COLLATE pg_catalog."default",
    private_latitude double precision,
    private_longitude double precision,
    public_positional_accuracy integer,
    geoprivacy text COLLATE pg_catalog."default",
    taxon_geoprivacy text COLLATE pg_catalog."default",
    coordinates_obscured boolean,
    positioning_method text COLLATE pg_catalog."default",
    positioning_device text COLLATE pg_catalog."default",
    species_guess text COLLATE pg_catalog."default",
    scientific_name text COLLATE pg_catalog."default",
    common_name text COLLATE pg_catalog."default",
    iconic_taxon_name text COLLATE pg_catalog."default",
    taxon_id integer,
    taxon_kingdom_name text COLLATE pg_catalog."default",
    taxon_phylum_name text COLLATE pg_catalog."default",
    taxon_class_name text COLLATE pg_catalog."default",
    taxon_order_name text COLLATE pg_catalog."default",
    taxon_family_name text COLLATE pg_catalog."default",
    taxon_genus_name text COLLATE pg_catalog."default",
    taxon_species_name text COLLATE pg_catalog."default",
    wov_taxa_id integer,
    CONSTRAINT wov_inaturalist_taxa_fk FOREIGN KEY (taxon_id)
        REFERENCES elog.wov_inaturalist_taxa (inaturalist_taxa_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT wov_taxa_fk FOREIGN KEY (wov_taxa_id)
        REFERENCES elog.wov_taxa (taxa_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS elog.wov_inaturalist_observations
    OWNER to app_user;

—------------------------------------------------------

-- Table: elog.wov_inaturalist_taxa

-- DROP TABLE IF EXISTS elog.wov_inaturalist_taxa;

CREATE TABLE IF NOT EXISTS elog.wov_inaturalist_taxa
(
    id integer NOT NULL DEFAULT nextval('elog.wov_inaturalist_taxa_id_seq'::regclass),
    taxonid character varying COLLATE pg_catalog."default",
    identifier character varying COLLATE pg_catalog."default",
    parentnameusageid character varying COLLATE pg_catalog."default",
    kingdom character varying COLLATE pg_catalog."default",
    phylum character varying COLLATE pg_catalog."default",
    class character varying COLLATE pg_catalog."default",
    "order" character varying COLLATE pg_catalog."default",
    family character varying COLLATE pg_catalog."default",
    genus character varying COLLATE pg_catalog."default",
    specificepithet character varying COLLATE pg_catalog."default",
    infraspecificepithet character varying COLLATE pg_catalog."default",
    modified character varying COLLATE pg_catalog."default",
    scientificname character varying COLLATE pg_catalog."default",
    taxonrank character varying COLLATE pg_catalog."default",
    "references" character varying COLLATE pg_catalog."default",
    inaturalist_taxa_id integer,
    CONSTRAINT wov_inaturalist_taxa_pkey PRIMARY KEY (id),
    CONSTRAINT taxa_id UNIQUE (inaturalist_taxa_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS elog.wov_inaturalist_taxa
    OWNER to app_user;
-- Index: idx_scientificname

-- DROP INDEX IF EXISTS elog.idx_scientificname;

CREATE INDEX IF NOT EXISTS idx_scientificname
    ON elog.wov_inaturalist_taxa USING btree
    (scientificname COLLATE pg_catalog."default" ASC NULLS LAST)
    INCLUDE(scientificname)
    TABLESPACE pg_default;
-- Index: idx_taxa_id

-- DROP INDEX IF EXISTS elog.idx_taxa_id;

CREATE INDEX IF NOT EXISTS idx_taxa_id
    ON elog.wov_inaturalist_taxa USING btree
    (inaturalist_taxa_id ASC NULLS LAST)
    TABLESPACE pg_default;


—------------------------------------------------------

-- Table: elog.wov_taxa

-- DROP TABLE IF EXISTS elog.wov_taxa;

CREATE TABLE IF NOT EXISTS elog.wov_taxa
(
    taxa_id integer NOT NULL DEFAULT nextval('elog.wov_taxa_taxa_id_seq'::regclass),
    original_name text COLLATE pg_catalog."default",
    matched_canonical text COLLATE pg_catalog."default",
    matched_name text COLLATE pg_catalog."default",
    source_key text COLLATE pg_catalog."default",
    current_name text COLLATE pg_catalog."default",
    current_canonical text COLLATE pg_catalog."default",
    synonym text COLLATE pg_catalog."default",
    data_source_id text COLLATE pg_catalog."default",
    data_source_title text COLLATE pg_catalog."default",
    current_classification_path text COLLATE pg_catalog."default",
    joined_name text COLLATE pg_catalog."default",
    source text COLLATE pg_catalog."default",
    level text COLLATE pg_catalog."default",
    current_base_name text COLLATE pg_catalog."default",
    current_source text COLLATE pg_catalog."default",
    taxonomy_kingdom text COLLATE pg_catalog."default",
    taxonomy_phylum text COLLATE pg_catalog."default",
    taxonomy_class text COLLATE pg_catalog."default",
    taxonomy_order text COLLATE pg_catalog."default",
    taxonomy_family text COLLATE pg_catalog."default",
    taxonomy_genus text COLLATE pg_catalog."default",
    citation text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    wikipedia_url text COLLATE pg_catalog."default",
    inaturalist_taxa_id integer,
    CONSTRAINT wov_taxa_pkey PRIMARY KEY (taxa_id),
    CONSTRAINT fk_wov_intaturalist_taxa FOREIGN KEY (inaturalist_taxa_id)
        REFERENCES elog.wov_inaturalist_taxa (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS elog.wov_taxa
    OWNER to app_user;
-- Index: idx_matched_canonical

-- DROP INDEX IF EXISTS elog.idx_matched_canonical;

CREATE INDEX IF NOT EXISTS idx_matched_canonical
    ON elog.wov_taxa USING btree
    (matched_canonical COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default

in addition we will need a user table and and for observations the voyage ID needs to be added. these are strings of 10 character length. 

describe any other tables you think the project might need

Thank you for providing the schema details — they reflect a thoughtful early design closely aligned with the core goals of the **Nuyina Wildlife Observation System**: supporting structured and casual observations, taxonomic linking, and integration with external platforms like iNaturalist.

Here’s a **draft Data Design Document (v0.2.0)**, which includes:

- Entity definitions for existing tables.
- Relationships and key design intent.
- Recommendations for additional tables and justification.
- Notes on data governance and export extensibility.

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

And yes — if you have a few rows of data from `wov_inaturalist_observations` or `wov_taxa`, I’d be happy to include them to enrich the document.

Let me know and I’ll expand this document/output further.

Citations:
[1] docker-compose.yml https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/3871842/fb6ca245-09fc-4e29-9f88-7c3e53ac3373/docker-compose.yml
