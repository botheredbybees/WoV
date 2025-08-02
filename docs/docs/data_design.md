I'mcan you draft a data design document. here are the tables I already have set up for this project. would you like examples of the data in any of them?
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


wox_taxa

"taxa_id","original_name","matched_canonical","matched_name","source_key","current_name","current_canonical","synonym","data_source_id","data_source_title","current_classification_path","joined_name","source","level","current_base_name","current_source","taxonomy_kingdom","taxonomy_phylum","taxonomy_class","taxonomy_order","taxonomy_family","taxonomy_genus","citation","description","wikipedia_url","inaturalist_taxa_id"
1,"[non-Uristidae] albinus","[non-Uristidae] albinus","[non-Uristidae] albinus (K.H. Barnard, 1932)","urn:lsid:marinespecies.org:taxname:875567","[non-Uristidae] albinus (K.H. Barnard, 1932)","[non-Uristidae] albinus","True","9","WoRMS","Animalia|Arthropoda|Malacostraca|Amphipoda|Uristidae|Uristes","Uristes albinus","(K.H. Barnard, 1932)","Species","[non-Uristidae] albinus","(K.H. Barnard, 1932)","Animalia","Arthropoda","Malacostraca","Amphipoda","Lysianassoidea incertae sedis",NULL,"Horton, T.; Lowry, J.; De Broyer, C.; Bellan-Santini, D.; Copilaş-Ciocianu, D.; Corbari, L.; Costello, M.J.; Daneliya, M.; Dauvin, J.-C.; Fišer, C.; Gasca, R.; Grabowski, M.; Guerra-García, J.M.; Hendrycks, E.; Hughes, L.; Jaume, D.; Jazdzewski, K.; Kim, Y.-H.; King, R.; Krapp-Schickel, T.; LeCroy, S.; Lörz, A.-N.; Mamos, T.; Senna, A.R.; Serejo, C.; Souza-Filho, J.F.; Tandberg, A.H.; Thomas, J.D.; Thurston, M.; Vader, W.; Väinölä, R.; Valls Domedel, G.; Vonk, R.; White, K.; Zeidler, W. (2024). World Amphipoda Database. Uristes albinus (K.H. Barnard, 1932). Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=237068 on 2024-05-09","","",NULL
2,"[non-Uristidae] georgianus","[non-Uristidae] georgianus","[non-Uristidae] georgianus (Schellenberg, 1931)","urn:lsid:marinespecies.org:taxname:875569","[non-Uristidae] georgianus (Schellenberg, 1931)","[non-Uristidae] georgianus","True","9","WoRMS","Animalia|Arthropoda|Malacostraca|Amphipoda|Uristidae|Uristes","Uristes georgianus","(Schellenberg, 1931)","Species","[non-Uristidae] georgianus","(Schellenberg, 1931)","Animalia","Arthropoda","Malacostraca","Amphipoda","Lysianassoidea incertae sedis",NULL,"Horton, T.; Lowry, J.; De Broyer, C.; Bellan-Santini, D.; Copilaş-Ciocianu, D.; Corbari, L.; Costello, M.J.; Daneliya, M.; Dauvin, J.-C.; Fišer, C.; Gasca, R.; Grabowski, M.; Guerra-García, J.M.; Hendrycks, E.; Hughes, L.; Jaume, D.; Jazdzewski, K.; Kim, Y.-H.; King, R.; Krapp-Schickel, T.; LeCroy, S.; Lörz, A.-N.; Mamos, T.; Senna, A.R.; Serejo, C.; Souza-Filho, J.F.; Tandberg, A.H.; Thomas, J.D.; Thurston, M.; Vader, W.; Väinölä, R.; Valls Domedel, G.; Vonk, R.; White, K.; Zeidler, W. (2024). World Amphipoda Database. Uristes georgianus (Schellenberg, 1931). Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=237212 on 2024-05-09","","",NULL
3,"Abatus (Pseudabatus) nimrodi","Abatus (Pseudabatus) nimrodi","Abatus (Pseudabatus) nimrodi (Koehler, 1911)","urn:lsid:marinespecies.org:taxname:513801","Abatus (Pseudabatus) nimrodi (Koehler, 1911)","Abatus (Pseudabatus) nimrodi","False","9","WoRMS","Animalia|Echinodermata|Echinoidea|Spatangoida|Schizasteridae|Abatus|Abatus nimrodi","Abatus nimrodi","(Koehler, 1911)","Species","Abatus (Pseudabatus) nimrodi","(Koehler, 1911)","Animalia","Echinodermata","Echinoidea","Spatangoida","Schizasteridae","Abatus","Kroh, A.; Mooi, R. (2024). World Echinoidea Database. Abatus nimrodi (Koehler, 1911). Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=160767 on 2024-05-09","","",NULL
4,"Abatus ingens","Abatus ingens","Abatus ingens Koehler, 1926","urn:lsid:marinespecies.org:taxname:160766","Abatus ingens Koehler, 1926","Abatus ingens","False","9","WoRMS","Animalia|Echinodermata|Echinoidea|Spatangoida|Schizasteridae|Abatus|Abatus ingens","Abatus ingens","Koehler, 1926","Species","Abatus ingens","Koehler, 1926","Animalia","Echinodermata","Echinoidea","Spatangoida","Schizasteridae","Abatus","Kroh, A.; Mooi, R. (2024). World Echinoidea Database. Abatus ingens Koehler, 1926. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=160766 on 2024-05-09","Abatus ingens is a species of sea urchin of the family Schizasteridae. Their armour is covered with spines. It is in the genus Abatus and lives in the sea. Abatus ingens was first scientifically described in 1926 by Koehler.




== References ==","https://en.wikipedia.org/wiki/Abatus_ingens",940918
5,"Abatus nimrodi","Abatus nimrodi","Abatus (Pseudabatus) nimrodi (Koehler, 1911)","urn:lsid:marinespecies.org:taxname:513801","Abatus (Pseudabatus) nimrodi (Koehler, 1911)","Abatus (Pseudabatus) nimrodi","False","9","WoRMS","Animalia|Echinodermata|Echinoidea|Spatangoida|Schizasteridae|Abatus|Abatus nimrodi","Abatus nimrodi","(Koehler, 1911)","Species","Abatus (Pseudabatus) nimrodi","(Koehler, 1911)","Animalia","Echinodermata","Echinoidea","Spatangoida","Schizasteridae","Abatus","Kroh, A.; Mooi, R. (2024). World Echinoidea Database. Abatus nimrodi (Koehler, 1911). Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=160767 on 2024-05-09","","",NULL
6,"Abatus philippii","Abatus philippii","Abatus philippii Lovén, 1871","urn:lsid:marinespecies.org:taxname:160768","Abatus philippii Lovén, 1871","Abatus philippii","False","9","WoRMS","Animalia|Echinodermata|Echinoidea|Spatangoida|Schizasteridae|Abatus|Abatus philippii","Abatus philippii","Lovén, 1871","Species","Abatus philippii","Lovén, 1871","Animalia","Echinodermata","Echinoidea","Spatangoida","Schizasteridae","Abatus","Kroh, A.; Mooi, R. (2024). World Echinoidea Database. Abatus philippii Lovén, 1871. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=160768 on 2024-05-09","Abatus philippii is a species of sea urchin of the family Schizasteridae. Their armour is covered with spines. It is in the genus Abatus and lives in the oceans of the southern hemisphere. Abatus philippii was first scientifically described in 1871 by Sven Lovén.




== References ==","https://en.wikipedia.org/wiki/Abatus_philippii",940923
7,"Abylidae","Abylidae","Abylidae L. Agassiz, 1862","urn:lsid:marinespecies.org:taxname:135336","Abylidae L. Agassiz, 1862","Abylidae","False","9","WoRMS","Animalia|Cnidaria|Hydrozoa|Siphonophorae|Abylidae","Abylidae","L. Agassiz, 1862","Family","Abylidae","L. Agassiz, 1862","Animalia","Cnidaria","Hydrozoa","Siphonophorae","Abylidae",NULL,"Schuchert, P. (2024). World Hydrozoa Database. Abylidae L. Agassiz, 1862. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=135336 on 2024-05-09","The Abylidae are a family of marine invertebrates in the order Siphonophorae. They are colonial, but the colonies can superficially resemble jellyfish; although they appear to be a single organism, each specimen is actually a colony of Siphonophora.
It contains the following taxa:


Subfamily Abylinae L. Agassiz, 1862
Genus Abyla Quoy & Gaimard, 1827
Abyla bicarinata Moser, 1925
Abyla haeckeli Lens & van Reimsdijk, 1908
Abyla trigona Quoy & Gaimard, 1827
Genus Ceratocymba Chun, 1888
Ceratocymba dentata (Bigelow, 1918)
Ceratocymba leuckarti (Huxley, 1859)
Ceratocymba sagittata Quoy & Gaimard, 1827
Subfamily Abylopsinae Totton, 1954
Genus Abylopsis Chun, 1888
Abylopsis eschscholtzi Huxley, 1859
Abylopsis tetragona Otto, 1823
Genus Bassia L. Agassiz, 1862
Bassia bassensis Quoy & Gaimard, 1827
Genus Enneagonum Quoy & Gaimard, 1827
Enneagonum hyalinum Quoy & Gaimard, 1827




== References ==","https://en.wikipedia.org/wiki/Abylidae",134248
8,"Acaena magellanica","Acaena magellanica","Acaena magellanica (Lam.) Vahl","5370832","Acaena magellanica (Lam.) Vahl","Acaena magellanica","False","11","GBIF Backbone Taxonomy","Plantae|Tracheophyta|Magnoliopsida|Rosales|Rosaceae|Acaena|Acaena magellanica","Acaena magellanica","(Lam.) Vahl","Species","Acaena magellanica","(Lam.) Vahl","Plantae","Tracheophyta","Magnoliopsida","Rosales","Rosaceae","Acaena","Acaena magellanica (Lam.) Vahl in GBIF Secretariat (2023). GBIF Backbone Taxonomy.  Checklist dataset https://doi.org/10.15468/39omei accessed via GBIF.org on 2024-05-27.","Acaena magellanica, commonly called buzzy burr or greater burnet, is a species of flowering plant whose range includes the southern tip of South America and many subantarctic islands.","https://en.wikipedia.org/wiki/Acaena_magellanica",51614
9,"Acaena magellanica pygmaea","Acaena magellanica","Acaena magellanica (Lam.) Vahl","5370832","Acaena magellanica (Lam.) Vahl","Acaena magellanica","False","11","GBIF Backbone Taxonomy","Plantae|Tracheophyta|Magnoliopsida|Rosales|Rosaceae|Acaena|Acaena magellanica","Acaena magellanica","(Lam.) Vahl","Species","Acaena magellanica","(Lam.) Vahl","Plantae","Tracheophyta","Magnoliopsida","Rosales","Rosaceae","Acaena","Acaena magellanica (Lam.) Vahl in GBIF Secretariat (2023). GBIF Backbone Taxonomy.  Checklist dataset https://doi.org/10.15468/39omei accessed via GBIF.org on 2024-05-27.","","",51614
10,"Acaena minor","Acaena minor","Acaena minor (Hook.fil.) Allan","5371118","Acaena minor (Hook.fil.) Allan","Acaena minor","False","11","GBIF Backbone Taxonomy","Plantae|Tracheophyta|Magnoliopsida|Rosales|Rosaceae|Acaena|Acaena minor","Acaena minor","(Hook.fil.) Allan","Species","Acaena minor","(Hook.fil.) Allan","Plantae","Tracheophyta","Magnoliopsida","Rosales","Rosaceae","Acaena","Acaena minor (Hook.fil.) Allan in GBIF Secretariat (2023). GBIF Backbone Taxonomy.  Checklist dataset https://doi.org/10.15468/39omei accessed via GBIF.org on 2024-05-27.","Acaena minor is a species of flowering plant whose range is confined to Australia's subantarctic Macquarie Island and to New Zealand's Campbell and Auckland Islands in the Southern Ocean.","https://en.wikipedia.org/wiki/Acaena_minor",292022
11,"Acaena minor var. antarctica","Acaena minor var. antarctica","Acaena minor var. antarcica (Cockayne) Allan, 1961","NZOR-6-29919#classification","Acaena minor var. antarcica (Cockayne) Allan, 1961","Acaena minor var. antarctica","False","11","GBIF Backbone Taxonomy","Plantae|Tracheophyta|Magnoliopsida|Rosales|Rosaceae|Acaena|Acaena minor","Acaena minor var. antarcica","(Cockayne) Allan, 1961","Variety","Acaena minor var. antarcica","(Cockayne) Allan, 1961","Plantae","Tracheophyta","Magnoliopsida","Rosales","Rosaceae","Acaena",NULL,"","",NULL
12,"Acanthaspidia longiramosa","Acanthaspidia longiramosa","Acanthaspidia longiramosa Vasina & Kussakin, 1982","urn:lsid:marinespecies.org:taxname:255625","Iolanthe longiramosa (Vasina & Kussakin, 1982)","Iolanthe longiramosa","True","9","WoRMS","Animalia|Arthropoda|Malacostraca|Isopoda|Acanthaspidiidae|Iolanthe|Iolanthe longiramosa","Acanthaspidia longiramosa","Vasina & Kussakin, 1982","Species","Iolanthe longiramosa","(Vasina & Kussakin, 1982)","Animalia","Arthropoda","Malacostraca","Isopoda","Acanthaspidiidae","Acanthaspidia","Boyko, C.B.; Bruce, N.L.; Hadfield, K.A.; Merrin, K.L.; Ota, Y.; Poore, G.C.B.; Taiti, S. (Eds) (2024). World Marine, Freshwater and Terrestrial Isopod Crustaceans database. Acanthaspidia longiramosa Vasina & Kussakin, 1982. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=255625 on 2024-05-10","","",NULL
13,"Acanthephyra","Acanthephyra","Acanthephyra A. Milne-Edwards, 1881","urn:lsid:marinespecies.org:taxname:107018","Acanthephyra A. Milne-Edwards, 1881","Acanthephyra","False","9","WoRMS","Animalia|Arthropoda|Malacostraca|Decapoda|Acanthephyridae|Acanthephyra","Acanthephyra","A. Milne-Edwards, 1881","Genus","Acanthephyra","A. Milne-Edwards, 1881","Animalia","Arthropoda","Malacostraca","Decapoda","Acanthephyridae","Acanthephyra","DecaNet eds. (2024). DecaNet. Acanthephyra A. Milne-Edwards, 1881. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=107018 on 2024-05-09","Acanthephyra is a genus of shrimp in the family Acanthephyridae, with species that live at depths from 0 to more than 5000 meters deep below the ocean surface.","https://en.wikipedia.org/wiki/Acanthephyra",336247
14,"Acanthephyra haeckeli","Acanthephyra pelagica","Acanthephyra pelagica (Risso, 1816)","urn:lsid:marinespecies.org:taxname:107581","Acanthephyra pelagica (Risso, 1816)","Acanthephyra pelagica","True","9","WoRMS","Animalia|Arthropoda|Malacostraca|Decapoda|Acanthephyridae|Acanthephyra","Acanthephyra pelagica","(Risso, 1816)","Species","Acanthephyra pelagica","(Risso, 1816)","Animalia","Arthropoda","Malacostraca","Decapoda","Acanthephyridae","Acanthephyra","DecaNet eds. (2024). DecaNet. Acanthephyra pelagica (Risso, 1816). Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=107581 on 2024-05-09","","",336276
15,"Acanthephyra pelagica","Acanthephyra pelagica","Acanthephyra pelagica (Risso, 1816)","urn:lsid:marinespecies.org:taxname:107581","Acanthephyra pelagica (Risso, 1816)","Acanthephyra pelagica","False","9","WoRMS","Animalia|Arthropoda|Malacostraca|Decapoda|Acanthephyridae|Acanthephyra|Acanthephyra pelagica","Acanthephyra pelagica","(Risso, 1816)","Species","Acanthephyra pelagica","(Risso, 1816)","Animalia","Arthropoda","Malacostraca","Decapoda","Acanthephyridae","Acanthephyra","DecaNet eds. (2024). DecaNet. Acanthephyra pelagica (Risso, 1816). Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=107581 on 2024-05-10","","",336276
16,"Acanthistius brasilianus","Acanthistius brasilianus","Acanthistius brasilianus (Cuvier, 1828)","urn:lsid:marinespecies.org:taxname:278720","Acanthistius brasilianus (Cuvier, 1828)","Acanthistius brasilianus","False","9","WoRMS","Animalia|Chordata|Teleostei|Perciformes|Serranidae|Acanthistius|Acanthistius brasilianus","Acanthistius brasilianus","(Cuvier, 1828)","Species","Acanthistius brasilianus","(Cuvier, 1828)","Animalia","Chordata","Teleostei","Perciformes","Serranidae","Acanthistius","Froese, R. and D. Pauly. Editors. (2024). FishBase. Acanthistius brasilianus (Cuvier, 1828). Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=278720 on 2024-05-09","The Argentine seabass (Acanthistius brasilianus) is a species of seabass in the family Serranidae. It occurs on the South American continental shelf of the western Atlantic Ocean, where it used to be caught commercially for human consumption.","https://en.wikipedia.org/wiki/Argentine_seabass",59805
17,"Acanthocorbis","Acanthocorbis","Acanthocorbis S.Hara & E.Takahashi, 1984","urn:lsid:marinespecies.org:taxname:105501","Acanthocorbis S.Hara & E.Takahashi, 1984","Acanthocorbis","False","9","WoRMS","Protozoa|Choanozoa|Choanoflagellatea|Acanthoecida|Acanthoecidae|Acanthocorbis","Acanthocorbis","S.Hara & E.Takahashi, 1984","Genus","Acanthocorbis","S.Hara & E.Takahashi, 1984","Protozoa","Choanozoa","Choanoflagellatea","Acanthoecida","Acanthoecidae","Acanthocorbis","Guiry, M.D. & Guiry, G.M. (2024). AlgaeBase. World-wide electronic publication, National University of Ireland, Galway (taxonomic information republished from AlgaeBase with permission of M.D. Guiry). Acanthocorbis S.Hara & E.Takahashi, 1984. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=105501 on 2024-05-09","Acanthocorbis is a genus of choanoflagellates within the family Acanthoecidae.","https://en.wikipedia.org/wiki/Acanthocorbis",NULL
18,"Acanthocorbis tinitinnabulum","Acanthocorbis tintinnabulum","Acanthocorbis tintinnabulum Marchant, van den Hoff & Burton, 1987","urn:lsid:marinespecies.org:taxname:341618","Acanthocorbis tintinnabulum Marchant, van den Hoff & Burton, 1987","Acanthocorbis tintinnabulum","False","9","WoRMS","Protozoa|Choanozoa|Choanoflagellatea|Acanthoecida|Acanthoecidae|Acanthocorbis|Acanthocorbis tintinnabulum","Acanthocorbis tintinnabulum","Marchant, van den Hoff & Burton, 1987","Species","Acanthocorbis tintinnabulum","Marchant, van den Hoff & Burton, 1987","Protozoa","Choanozoa","Choanoflagellatea","Acanthoecida","Acanthoecidae","Acanthocorbis","WoRMS (2024). Acanthocorbis tintinnabulum Marchant, van den Hoff & Burton, 1987. Accessed at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=341618 on 2024-05-09","","",NULL
19,"Acanthocorbis tintinnabulum","Acanthocorbis tintinnabulum","Acanthocorbis tintinnabulum Marchant, van den Hoff & Burton, 1987","urn:lsid:marinespecies.org:taxname:341618","Acanthocorbis tintinnabulum Marchant, van den Hoff & Burton, 1987","Acanthocorbis tintinnabulum","False","9","WoRMS","Protozoa|Choanozoa|Choanoflagellatea|Acanthoecida|Acanthoecidae|Acanthocorbis|Acanthocorbis tintinnabulum","Acanthocorbis tintinnabulum","Marchant, van den Hoff & Burton, 1987","Species","Acanthocorbis tintinnabulum","Marchant, van den Hoff & Burton, 1987","Protozoa","Choanozoa","Choanoflagellatea","Acanthoecida","Acanthoecidae","Acanthocorbis","WoRMS (2024). Acanthocorbis tintinnabulum Marchant, van den Hoff & Burton, 1987. Accessed at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=341618 on 2024-05-09","","",NULL
20,"Acanthocorbis unguiculata","Acanthocorbis unguiculata","Acanthocorbis unguiculata (Thomsen) Hara & Takahashi, 1984","4378236","Acanthocorbis unguiculata (Thomsen) Hara & Takahashi, 1984","Acanthocorbis unguiculata","False","11","GBIF Backbone Taxonomy","Protozoa|Choanozoa|Choanoflagellatea|Choanoflagellida|Acanthoecidae|Acanthocorbis|Acanthocorbis unguiculata","Acanthocorbis unguiculata (Thomsen) Hara & Takahashi, 1984","(Thomsen) Hara & Takahashi, 1984","Species","Acanthocorbis unguiculata","(Thomsen) Hara & Takahashi, 1984","Protozoa","Choanozoa","Choanoflagellatea","Choanoflagellida","Acanthoecidae","Acanthocorbis","Acanthocorbis unguiculata (Thomsen) Hara & Takahashi, 1984 in GBIF Secretariat (2023). GBIF Backbone Taxonomy.  Checklist dataset https://doi.org/10.15468/39omei accessed via GBIF.org on 2024-05-27.","","",NULL
21,"Acanthocyclops mirnyi","Acanthocyclops mirnyi","Acanthocyclops mirnyi Borutzky & Vinogradov, 1957","urn:lsid:marinespecies.org:taxname:348422","Diacyclops mirnyi (Borutzky & Vinogradov, 1957)","Diacyclops mirnyi","True","9","WoRMS","Animalia|Arthropoda|Copepoda|Cyclopoida|Cyclopidae|Diacyclops|Diacyclops mirnyi","Acanthocyclops mirnyi","Borutzky & Vinogradov, 1957","Species","Diacyclops mirnyi","(Borutzky & Vinogradov, 1957)","Animalia","Arthropoda","Copepoda","Cyclopoida","Cyclopidae","Acanthocyclops","Walter, T.C.; Boxshall, G. (2024). World of Copepods Database. Acanthocyclops mirnyi Borutzky & Vinogradov, 1957. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=348422 on 2024-05-10","","",NULL
22,"Acanthocystis","Acanthocystis","Acanthocystis","urn:lsid:marinespecies.org:taxname:341276","Acanthocystis","Acanthocystis","False","9","WoRMS","Chromista|Heliozoa|Centrohelea|Centrohelida|Acanthocystidae|Acanthocystis","Acanthocystis",NULL,"Genus","Acanthocystis",NULL,"Chromista","Heliozoa","Centrohelea","Centrohelida","Acanthocystidae","Acanthocystis","WoRMS (2024). Acanthocystis. Accessed at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=341276 on 2024-05-10","","",271161
23,"Acanthoeca spectabilis","Acanthoeca spectabilis","Acanthoeca spectabilis Ellis, 1930","4270005","Acanthoeca spectabilis Ellis, 1930","Acanthoeca spectabilis","False","11","GBIF Backbone Taxonomy","Protozoa|Choanozoa|Choanoflagellatea|Choanoflagellida|Acanthoecidae|Acanthoeca|Acanthoeca spectabilis","Acanthoeca spectabilis Ellis, 1930","Ellis, 1930","Species","Acanthoeca spectabilis","Ellis, 1930","Protozoa","Choanozoa","Choanoflagellatea","Choanoflagellida","Acanthoecidae","Acanthoeca","Acanthoeca spectabilis Ellis, 1930 in GBIF Secretariat (2023). GBIF Backbone Taxonomy.  Checklist dataset https://doi.org/10.15468/39omei accessed via GBIF.org on 2024-05-27.","","",NULL
24,"Acanthoica quattrospina","Acanthoica quattrospina","Acanthoica quattrospina Lohmann, 1903","3202169","Acanthoica quattrospina Lohmann, 1903","Acanthoica quattrospina","False","11","GBIF Backbone Taxonomy","Chromista|Haptophyta|Prymnesiophyceae|Syracosphaerales|Rhabdosphaeraceae|Acanthoica|Acanthoica quattrospina","Acanthoica quattrospina Lohmann, 1903","Lohmann, 1903","Species","Acanthoica quattrospina","Lohmann, 1903","Chromista","Haptophyta","Prymnesiophyceae","Syracosphaerales","Rhabdosphaeraceae","Acanthoica","Acanthoica quattrospina Lohmann, 1903 in GBIF Secretariat (2023). GBIF Backbone Taxonomy.  Checklist dataset https://doi.org/10.15468/39omei accessed via GBIF.org on 2024-05-27.","Acanthoica quattrospina is a species of alga belonging to the family Rhabdosphaeraceae.
It has cosmopolitan distribution.




== References ==","https://en.wikipedia.org/wiki/Acanthoica_quattrospina",790375
25,"Acanthonotozomatidae","Acanthonotozomatidae","Acanthonotozomatidae Stebbing, 1906","101362","Acanthonotozomatidae Stebbing, 1906","Acanthonotozomatidae","False","9","WoRMS","Animalia|Arthropoda|Malacostraca|Amphipoda|Iphimedioidea|Acanthonotozomatidae","Acanthonotozomatidae","Stebbing, 1906","Family","Acanthonotozomatidae","Stebbing, 1906","Animalia","Arthropoda","Malacostraca","Amphipoda","Acanthonotozomatidae",NULL,"Horton, T.; Lowry, J.; De Broyer, C.; Bellan-Santini, D.; Copilas-Ciocianu, D.; Corbari, L.; Costello, M.J.; Daneliya, M.; Dauvin, J.-C.; Fišer, C.; Gasca, R.; Grabowski, M.; Guerra-García, J.M.; Hendrycks, E.; Hughes, L.; Jaume, D.; Jazdzewski, K.; Kim, Y.-H.; King, R.; Krapp-Schickel, T.; LeCroy, S.; Lörz, A.-N.; Mamos, T.; Senna, A.R.; Serejo, C.; Souza-Filho, J.F.; Tandberg, A.H.; Thomas, J.D.; Thurston, M.; Vader, W.; Väinölä, R.; Valls Domedel, G.; Vonk, R.; White, K.; Zeidler, W. (2024). World Amphipoda Database. Acanthonotozomatidae Stebbing, 1906. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=101362 on 2024-05-31","Acanthonotozomatidae is a family of amphipod crustaceans, which currently comprises the single genus Acanthonotozoma Boeck, 1876.




== References ==","https://en.wikipedia.org/wiki/Acanthonotozoma",244559
26,"Acarospora gwynnii","Acarospora gwynnii","Acarospora gwynnii C.W. Dodge & E.D. Rudolph, 1955","urn:lsid:marinespecies.org:taxname:1603898","Acarospora gwynnii C.W. Dodge & E.D. Rudolph, 1955","Acarospora gwynnii","False","9","WoRMS","Fungi|Ascomycota|Lecanoromycetes|Acarosporales|Acarosporaceae|Acarospora|Acarospora gwynnii","Acarospora gwynnii","C.W. Dodge & E.D. Rudolph, 1955","Species","Acarospora gwynnii","C.W. Dodge & E.D. Rudolph, 1955","Fungi","Ascomycota","Lecanoromycetes","Acarosporales","Acarosporaceae","Acarospora","Index Fungorum Partnership (2024). Index Fungorum. Acarospora gwynnii C.W. Dodge & E.D. Rudolph, 1955. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=1603898 on 2024-05-09","","",NULL
27,"Acarospora macrocyclos","Acarospora macrocyclos","Acarospora macrocyclos Vain., 1903","urn:lsid:marinespecies.org:taxname:1603899","Acarospora macrocyclos Vain., 1903","Acarospora macrocyclos","False","9","WoRMS","Fungi|Ascomycota|Lecanoromycetes|Acarosporales|Acarosporaceae|Acarospora|Acarospora macrocyclos","Acarospora macrocyclos","Vain., 1903","Species","Acarospora macrocyclos","Vain., 1903","Fungi","Ascomycota","Lecanoromycetes","Acarosporales","Acarosporaceae","Acarospora","Index Fungorum Partnership (2024). Index Fungorum. Acarospora macrocyclos Vain., 1903. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=1603899 on 2024-05-09","","",684941
28,"Acarospora williamsii","Acarospora williamsii","Acarospora williamsii Filson, 1966","urn:lsid:marinespecies.org:taxname:1603903","Acarospora williamsii Filson, 1966","Acarospora williamsii","False","9","WoRMS","Fungi|Ascomycota|Lecanoromycetes|Acarosporales|Acarosporaceae|Acarospora|Acarospora williamsii","Acarospora williamsii","Filson, 1966","Species","Acarospora williamsii","Filson, 1966","Fungi","Ascomycota","Lecanoromycetes","Acarosporales","Acarosporaceae","Acarospora","Index Fungorum Partnership (2024). Index Fungorum. Acarospora williamsii Filson, 1966. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=1603903 on 2024-05-09","","",NULL
29,"Acartia","Acartia","Acartia Dana, 1846","urn:lsid:marinespecies.org:taxname:104108","Acartia Dana, 1846","Acartia","False","9","WoRMS","Animalia|Arthropoda|Copepoda|Calanoida|Acartiidae|Acartia","Acartia","Dana, 1846","Genus","Acartia","Dana, 1846","Animalia","Arthropoda","Copepoda","Calanoida","Acartiidae","Acartia","Walter, T.C.; Boxshall, G. (2024). World of Copepods Database. Acartia Dana, 1846. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=104108 on 2024-05-09","Acartia is a genus of marine calanoid copepods. They are epipelagic, estuarine, zooplanktonic  found throughout the oceans of the world, primarily in temperate regions.","https://en.wikipedia.org/wiki/Acartia",133949
30,"Acartia (Acartia) danae","Acartia (Acartia) danae","Acartia (Acartia) danae Giesbrecht, 1889","urn:lsid:marinespecies.org:taxname:346026","Acartia (Acartia) danae Giesbrecht, 1889","Acartia (Acartia) danae","False","9","WoRMS","Animalia|Arthropoda|Copepoda|Calanoida|Acartiidae|Acartia|Acartia danae","Acartia danae","Giesbrecht, 1889","Species","Acartia (Acartia) danae","Giesbrecht, 1889","Animalia","Arthropoda","Copepoda","Calanoida","Acartiidae","Acartia","Walter, T.C.; Boxshall, G. (2024). World of Copepods Database. Acartia danae Giesbrecht, 1889. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=104252 on 2024-05-09","","",NULL
31,"Acartia danae","Acartia (Acartia) danae","Acartia (Acartia) danae Giesbrecht, 1889","urn:lsid:marinespecies.org:taxname:346026","Acartia (Acartia) danae Giesbrecht, 1889","Acartia (Acartia) danae","False","9","WoRMS","Animalia|Arthropoda|Copepoda|Calanoida|Acartiidae|Acartia|Acartia danae","Acartia danae","Giesbrecht, 1889","Species","Acartia (Acartia) danae","Giesbrecht, 1889","Animalia","Arthropoda","Copepoda","Calanoida","Acartiidae","Acartia","Walter, T.C.; Boxshall, G. (2024). World of Copepods Database. Acartia danae Giesbrecht, 1889. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=104252 on 2024-05-09","","",NULL
32,"Acartia (Acartiura) tranteri","Acartia (Acartiura) tranteri","Acartia (Acartiura) tranteri Bradford, 1976","urn:lsid:marinespecies.org:taxname:346042","Acartia (Acartiura) tranteri Bradford, 1976","Acartia (Acartiura) tranteri","False","9","WoRMS","Animalia|Arthropoda|Copepoda|Calanoida|Acartiidae|Acartia|Acartia tranteri","Acartia tranteri","Bradford, 1976","Species","Acartia (Acartiura) tranteri","Bradford, 1976","Animalia","Arthropoda","Copepoda","Calanoida","Acartiidae","Acartia","Walter, T.C.; Boxshall, G. (2024). World of Copepods Database. Acartia tranteri Bradford, 1976. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=348528 on 2024-05-09","","",NULL
33,"Acartia tranteri","Acartia (Acartiura) tranteri","Acartia (Acartiura) tranteri Bradford, 1976","urn:lsid:marinespecies.org:taxname:346042","Acartia (Acartiura) tranteri Bradford, 1976","Acartia (Acartiura) tranteri","False","9","WoRMS","Animalia|Arthropoda|Copepoda|Calanoida|Acartiidae|Acartia|Acartia tranteri","Acartia tranteri","Bradford, 1976","Species","Acartia (Acartiura) tranteri","Bradford, 1976","Animalia","Arthropoda","Copepoda","Calanoida","Acartiidae","Acartia","Walter, T.C.; Boxshall, G. (2024). World of Copepods Database. Acartia tranteri Bradford, 1976. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=348528 on 2024-05-09","Acartia tranteri is a species of marine copepod belonging to the family Acartiidae. This Australian species is related to the New Zealand species A. ensifera, A. jilletti and A. simplex but can be distinguished by the lack of any ventral prominence posterior to the genital opening in the female and the presence of posterior spines on the metasome (body segment) of the male. It is found off the southern coast of Australia (New South Wales).","https://en.wikipedia.org/wiki/Acartia_tranteri",NULL
34,"Acartia (Odontacartia) pacifica","Acartia (Odontacartia) pacifica","Acartia (Odontacartia) pacifica Steuer, 1915","urn:lsid:marinespecies.org:taxname:346059","Acartia (Odontacartia) pacifica Steuer, 1915","Acartia (Odontacartia) pacifica","False","9","WoRMS","Animalia|Arthropoda|Copepoda|Calanoida|Acartiidae|Acartia|Acartia pacifica","Acartia pacifica","Steuer, 1915","Species","Acartia (Odontacartia) pacifica","Steuer, 1915","Animalia","Arthropoda","Copepoda","Calanoida","Acartiidae","Acartia","Walter, T.C.; Boxshall, G. (2024). World of Copepods Database. Acartia pacifica Steuer, 1915. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=348516 on 2024-05-09","","",NULL
35,"Acartia pacifica","Acartia (Odontacartia) pacifica","Acartia (Odontacartia) pacifica Steuer, 1915","urn:lsid:marinespecies.org:taxname:346059","Acartia (Odontacartia) pacifica Steuer, 1915","Acartia (Odontacartia) pacifica","False","9","WoRMS","Animalia|Arthropoda|Copepoda|Calanoida|Acartiidae|Acartia|Acartia pacifica","Acartia pacifica","Steuer, 1915","Species","Acartia (Odontacartia) pacifica","Steuer, 1915","Animalia","Arthropoda","Copepoda","Calanoida","Acartiidae","Acartia","Walter, T.C.; Boxshall, G. (2024). World of Copepods Database. Acartia pacifica Steuer, 1915. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=348516 on 2024-05-09","","",NULL
36,"Achelia","Achelia","Achelia Hodge, 1864","urn:lsid:marinespecies.org:taxname:134568","Achelia Hodge, 1864","Achelia","False","9","WoRMS","Animalia|Arthropoda|Pycnogonida|Pantopoda|Ammotheidae|Achelia","Achelia","Hodge, 1864","Genus","Achelia","Hodge, 1864","Animalia","Arthropoda","Pycnogonida","Pantopoda","Ammotheidae","Achelia","Bamber, R.N.; El Nagar, A.; Arango, C.P. (Eds) (2024). Pycnobase: World Pycnogonida Database. Achelia Hodge, 1864. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=134568 on 2024-05-09","Achelia is a genus of pycnogonids in the family Ammotheidae.","https://en.wikipedia.org/wiki/Achelia",132286
37,"Achelia spicata","Achelia spicata","Achelia spicata (Hodgson, 1914)","urn:lsid:marinespecies.org:taxname:172865","Achelia spicata (Hodgson, 1914)","Achelia spicata","False","9","WoRMS","Animalia|Arthropoda|Pycnogonida|Pantopoda|Ammotheidae|Achelia|Achelia spicata","Achelia spicata","(Hodgson, 1914)","Species","Achelia spicata","(Hodgson, 1914)","Animalia","Arthropoda","Pycnogonida","Pantopoda","Ammotheidae","Achelia","Bamber, R.N.; El Nagar, A.; Arango, C.P. (Eds) (2024). Pycnobase: World Pycnogonida Database. Achelia spicata (Hodgson, 1914). Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=172865 on 2024-05-09","","",638448
38,"Achiridota","Achiridota","Achiridota H.L. Clark, 1908","urn:lsid:marinespecies.org:taxname:123437","Achiridota H.L. Clark, 1908","Achiridota","False","9","WoRMS","Animalia|Echinodermata|Holothuroidea|Apodida|Myriotrochidae|Achiridota","Achiridota","H.L. Clark, 1908","Genus","Achiridota","H.L. Clark, 1908","Animalia","Echinodermata","Holothuroidea","Apodida","Myriotrochidae","Achiridota","WoRMS (2024). Achiridota H.L. Clark, 1908. Accessed at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=123437 on 2024-05-09","","",940377
39,"Achnanthes","Achnanthes","Achnanthes Bory, 1822","urn:lsid:marinespecies.org:taxname:149191","Achnanthes Bory, 1822","Achnanthes","False","9","WoRMS","Chromista|Bacillariophyta|Bacillariophyceae|Achnanthales|Achnanthaceae|Achnanthes","Achnanthes","Bory, 1822","Genus","Achnanthes","Bory, 1822","Chromista","Bacillariophyta","Bacillariophyceae","Achnanthales","Achnanthaceae","Achnanthes","Kociolek, J.P.; Blanco, S.; Coste, M.; Ector, L.; Liu, Y.; Karthick, B.; Kulikovskiy, M.; Lundholm, N.; Ludwig, T.; Potapova, M.; Rimet, F.; Sabbe, K.; Sala, S.; Sar, E.; Taylor, J.; Van de Vijver, B.; Wetzel, C.E.; Williams, D.M.; Witkowski, A.; Witkowski, J. (2024). DiatomBase. Achnanthes Bory, 1822. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=149191 on 2024-05-09","Achnanthes is a genus of diatoms belonging to the family Achnanthaceae.
The genus was described in 1822 by Jean Baptiste Bory de Saint-Vincent.
The genus has cosmopolitan distribution.
Species:


Achnanthes aapajaervensis Cleve-Euler
Achnanthes abundans Manguin, 1954
Achnanthes acares Hohn & Hellerman
Achnanthes acus Simonsen
Achnanthes acuta Frenguelli




== References ==","https://en.wikipedia.org/wiki/Achnanthes",244685
40,"Achnanthes abundans","Achnanthes abundans","Achnanthes abundans Manguin in Bourrelly & Manguin, 1954","urn:lsid:marinespecies.org:taxname:611403","Psammothidium abundans (Manguin, Bourrelly & Manguin) L.Bukhtiyarova, 1996","Psammothidium abundans","True","9","WoRMS","Chromista|Bacillariophyta|Bacillariophyceae|Achnanthales|Achnanthaceae|Psammothidium|Pasmmothidium abundans","Achnanthes abundans","Manguin in Bourrelly & Manguin, 1954","Species","Psammothidium abundans","(Manguin, Bourrelly & Manguin) L.Bukhtiyarova, 1996","Chromista","Heterokontophyta","Bacillariophyceae","Achnanthales","Achnanthidiaceae","Psammothidium","Kociolek, J.P.; Blanco, S.; Coste, M.; Ector, L.; Liu, Y.; Karthick, B.; Kulikovskiy, M.; Lundholm, N.; Ludwig, T.; Potapova, M.; Rimet, F.; Sabbe, K.; Sala, S.; Sar, E.; Taylor, J.; Van de Vijver, B.; Wetzel, C.E.; Williams, D.M.; Witkowski, A.; Witkowski, J. (2024). DiatomBase. Psammothidium abundans (Manguin, Bourrelly & Manguin) L.Bukhtiyarova, 1996. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=610727 on 2024-05-31","","",NULL
41,"Achnanthes austriaca","Achnanthes austriaca","Achnanthes austriaca Hust., 1922","urn:lsid:marinespecies.org:taxname:178998","Achnanthes austriaca Hust., 1922","Achnanthes austriaca","False","9","WoRMS","Chromista|Bacillariophyta|Bacillariophyceae|Achnanthales|Achnanthaceae|Achnanthes|Achnanthes austriaca","Achnanthes austriaca","Hust., 1922","Species","Achnanthes austriaca","Hust., 1922","Chromista","Bacillariophyta","Bacillariophyceae","Achnanthales","Achnanthaceae","Achnanthes","Kociolek, J.P.; Blanco, S.; Coste, M.; Ector, L.; Liu, Y.; Karthick, B.; Kulikovskiy, M.; Lundholm, N.; Ludwig, T.; Potapova, M.; Rimet, F.; Sabbe, K.; Sala, S.; Sar, E.; Taylor, J.; Van de Vijver, B.; Wetzel, C.E.; Williams, D.M.; Witkowski, A.; Witkowski, J. (2024). DiatomBase. Achnanthes austriaca Hust., 1922. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=178998 on 2024-05-09","","",NULL
42,"Achnanthes brevipes","Achnanthes brevipes","Achnanthes brevipes C.Agardh, 1824","urn:lsid:marinespecies.org:taxname:149387","Achnanthes brevipes C.Agardh, 1824","Achnanthes brevipes","False","9","WoRMS","Chromista|Bacillariophyta|Bacillariophyceae|Achnanthales|Achnanthaceae|Achnanthes|Achnanthes brevipes","Achnanthes brevipes","C.Agardh, 1824","Species","Achnanthes brevipes","C.Agardh, 1824","Chromista","Bacillariophyta","Bacillariophyceae","Achnanthales","Achnanthaceae","Achnanthes","Kociolek, J.P.; Blanco, S.; Coste, M.; Ector, L.; Liu, Y.; Karthick, B.; Kulikovskiy, M.; Lundholm, N.; Ludwig, T.; Potapova, M.; Rimet, F.; Sabbe, K.; Sala, S.; Sar, E.; Taylor, J.; Van de Vijver, B.; Wetzel, C.E.; Williams, D.M.; Witkowski, A.; Witkowski, J. (2024). DiatomBase. Achnanthes brevipes C.Agardh, 1824. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=149387 on 2024-05-09","","",NULL
43,"Achnanthes brevipes var. intermedia","Achnanthes brevipes var. intermedia","Achnanthes brevipes var. intermedia (Kützing) Cleve, 1895","urn:lsid:marinespecies.org:taxname:160618","Achnanthes intermedia Kützing, 1833","Achnanthes intermedia","True","9","WoRMS","Chromista|Bacillariophyta|Bacillariophyceae|Achnanthales|Achnanthaceae|Achnanthes|Achnanthes intermedia","Achnanthes brevipes var. intermedia","(Kützing) Cleve, 1895","Variety","Achnanthes intermedia","Kützing, 1833","Chromista","Bacillariophyta","Bacillariophyceae","Achnanthales","Achnanthaceae","Achnanthes","Kociolek, J.P.; Blanco, S.; Coste, M.; Ector, L.; Liu, Y.; Karthick, B.; Kulikovskiy, M.; Lundholm, N.; Ludwig, T.; Potapova, M.; Rimet, F.; Sabbe, K.; Sala, S.; Sar, E.; Taylor, J.; Van de Vijver, B.; Wetzel, C.E.; Williams, D.M.; Witkowski, A.; Witkowski, J. (2024). DiatomBase. Achnanthes brevipes var. intermedia (Kützing) Cleve, 1895. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=160618 on 2024-05-09","","",NULL
44,"Achnanthes clevei","Achnanthes clevei","Achnanthes clevei Grunow, 1880","urn:lsid:marinespecies.org:taxname:160620","Karayevia clevei (Grunow) Round & Bukhtiyarova, 1999","Karayevia clevei","True","9","WoRMS","Chromista|Bacillariophyta|Bacillariophyceae|Achnanthales|Achnanthidiaceae|Karayevia|Karayevia clevei","Achnanthes clevei","Grunow, 1880","Species","Karayevia clevei","(Grunow) Round & Bukhtiyarova, 1999","Chromista","Bacillariophyta","Bacillariophyceae","Achnanthales","Achnanthaceae","Achnanthes","Kociolek, J.P.; Blanco, S.; Coste, M.; Ector, L.; Liu, Y.; Karthick, B.; Kulikovskiy, M.; Lundholm, N.; Ludwig, T.; Potapova, M.; Rimet, F.; Sabbe, K.; Sala, S.; Sar, E.; Taylor, J.; Van de Vijver, B.; Wetzel, C.E.; Williams, D.M.; Witkowski, A.; Witkowski, J. (2024). DiatomBase. Achnanthes clevei Grunow, 1880. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=160620 on 2024-05-09","","",NULL
45,"Achnanthes coarctata","Achnanthes coarctata","Achnanthes coarctata (Brébisson ex W.Smith) Grunow, 1880","urn:lsid:marinespecies.org:taxname:160622","Achnanthes coarctata (Brébisson ex W.Smith) Grunow, 1880","Achnanthes coarctata","False","9","WoRMS","Chromista|Bacillariophyta|Bacillariophyceae|Achnanthales|Achnanthaceae|Achnanthes|Achnanthes coarctata","Achnanthes coarctata","(Brébisson ex W.Smith) Grunow, 1880","Species","Achnanthes coarctata","(Brébisson ex W.Smith) Grunow, 1880","Chromista","Bacillariophyta","Bacillariophyceae","Achnanthales","Achnanthaceae","Achnanthes","Kociolek, J.P.; Blanco, S.; Coste, M.; Ector, L.; Liu, Y.; Karthick, B.; Kulikovskiy, M.; Lundholm, N.; Ludwig, T.; Potapova, M.; Rimet, F.; Sabbe, K.; Sala, S.; Sar, E.; Taylor, J.; Van de Vijver, B.; Wetzel, C.E.; Williams, D.M.; Witkowski, A.; Witkowski, J. (2024). DiatomBase. Achnanthes coarctata (Brébisson ex W.Smith) Grunow, 1880. Accessed through: World Register of Marine Species at: https://www.marinespecies.org/aphia.php?p=taxdetails&id=160622 on 2024-05-09","","",775836
46,"Achnanthes confusa","Achnanthes confusa","Achnanthes confusa Manguin","urn:lsid:marinespecies.org:taxname:633436","Achnanthes confusa Manguin","Achnanthes confusa","False","9","WoRMS","Chromista|Bacillariophyta|Bacillariophyceae|Achnanthales|Achnanthaceae|Achnanthes|Achnanthes confusa","Achnanthes confusa","Manguin","Species","Achnanthes confusa","Manguin","Chromista","Bacillariophyta","Bacillariophyceae","Achnanthales","Achnanthaceae","Achnanthes","Kociolek, J.P.; Blanco, S.; Coste, M.; Ector, L.; Liu, Y.; Karthick, B.; Kulikovskiy, M.; Lund

Thank you for sharing this sample of **`wov_taxa` table** data. It gives excellent insight into how you're modeling species records from multiple sources (e.g. WoRMS, GBIF, iNaturalist) and reconciling them locally.

Based on this sample, here's a **summary analysis** of what the table is doing and some **recommendations for refinement and integration** in the WoV schema.

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
