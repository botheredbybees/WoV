📊 Data Design Document: Nuyina Wildlife Observation System
📅 Drafted: August 2025
📦 Schema Version: 0.3.0
👤 Author: Platform development team (WoV project)

📘 Purpose
This document defines and documents the current and proposed database schema used within the Nuyina Wildlife Observation System (WoV). It is intended to guide ongoing development of:

Onboard data collection (structured + casual)

Taxonomic reconciliation

Attribution and licensing

Export support (iNaturalist, ALA, eBird)

Sensor-context integration

Offline resilience onboard RSV Nuyina

📐 Entity Definitions (Current)
1. wov.wov_dictionary
A central parameter dictionary for recorded variables (e.g., survey metadata, instrument types, data descriptors).

Field	Description
dictionary_id	Primary key
parameter_or_variable	Name used in field input or CSV
definition	Meaning or contextual explanation
units	Measurement units
sampling_instrument	Tool used to collect this data
standard	Format or guideline used (e.g., Darwin Core)
csv_files	Used for tracing to inputs/exports

Export to Sheets
🔎 Used internally for future automated mapping, validation or standardization.

2. wov.wov_inaturalist_taxa
Imported taxonomic metadata modeled on iNaturalist’s hierarchy and field conventions.

Field	Description
id	Local primary key
inaturalist_taxa_id	Unique iNat taxon ID
scientificname, genus...	Full taxonomic breakdown
reference_url, modified	Metadata support
taxonid, identifier	From iNaturalist

Export to Sheets
🔗 Connected via FK to wov_inaturalist_observations.

3. wov.wov_taxa
Locally resolved taxa from submitted observations, possibly matched via various external tools (e.g., GBIF, CoL).

Field	Description
taxa_id	Local ID — PK
original_name	Entered by observer
matched_name	System match
synonym, source_key, data_source_id	Resolution tracking
taxonomy_* fields	Classifications
inaturalist_taxa_id	Optional link (FK) if reconciled

Export to Sheets
🧠 Supports flexible resolution/workflow-based ID refinement.

4. wov.wov_users
Tracks users locally — shipboard accounts, authentication metadata, contributor roles.

Field	Description
user_id	Local unique identifier (UUID)
username	Display name
email	Optional (for verification/logging)
role	observer
created_at	Timestamp of signup
inaturalist_id	New column for iNaturalist user ID
upload_to_inaturalist	New column for iNaturalist upload preference
upload_to_ebird	New column for eBird upload preference

Export to Sheets
🔑 Required for crew/scientist-led access control and export traceability. Integrates with Supabase Auth (GoTrue).

5. wov.wov_voyages
Manage voyage metadata, dates, ship, route, and configuration.

Field	Description
voyage_id	10-character human-meaningful code (PK)
name	Optional long name e.g., "2025 Season 3"
start_date	Voyage commencement
end_date	Return date or expected end
region	Southern Ocean, Heard Island, etc.
notes	Optional freeform/log tracking

Export to Sheets
📎 Cross-linked to all related data (observations, summaries, sensor logs, exports).

6. wov.wov_inaturalist_observations
Observations imported from the iNat API or exported by users to iNat.

Field	Description
id	Remote ID (iNat assigned)
observed_on, time_observed_at	Local and ISO datetime
user_id, user_login, user_name	Author identifiers (possibly linked)
taxon_id, wov_taxa_id	Links to iNat and WoV taxonomic tables
latitude, longitude, accuracy	Geospatial fields
image_url, description, quality_grade	Rich metadata from iNat
license	Licensing info
voyage_id	Links to a specific voyage

Export to Sheets
🌐 Backbone of outbound sync/export with attribution.

7. wov.wov_observations
New table for storing shipboard-only sightings and data.

Field	Description
observation_id	Primary key
inaturalist_observation_id	External iNaturalist observation ID if applicable
observed_on	Date of observation
time_observed_at	Timestamp of observation
user_id	Foreign key to wov_users
user_login	User's login
species_guess	Species name guessed by observer
common_name	Common name of species
scientific_name	Scientific name of species
latitude, longitude	Geospatial coordinates
positional_accuracy	Accuracy of coordinates
wov_taxa_id	Foreign key to wov_taxa
taxon_id	Foreign key to wov_inaturalist_taxa
license	Licensing info
quality_grade	Data quality grade
description	Description of the observation
coordinates_obscured	Boolean to indicate if coordinates are obscured
voyage_id	Foreign key to wov_voyages
sea_surface_temp	Sea surface temperature from sensor data
wind_speed_true, wind_direction_true	Wind data from sensor data
air_temp	Air temperature from sensor data
salinity	Salinity from sensor data
distance_to_animals	Estimated distance to animals
group_size_estimate	Estimated group size of animals
vessel_speed, vessel_course	Vessel data from sensor data

Export to Sheets
8. wov.wov_images
Structured table for managing observer-submitted images.

Field	Description
image_id	Primary key (UUID)
observation_id	FK to wov_observations
file_path	Filesystem path or Supabase storage key
camera_model	From EXIF
datetime_original	From EXIF
license	Licensing info

Export to Sheets
📸 Helps link professional images back to observations with full metadata, including spatial accuracy.

🔄 Relationships Summary
Plaintext

wov_users <-- wov_observations --> wov_images
                |
                |--> wov_voyages
                |
                |--> wov_taxa --> wov_inaturalist_taxa
                |
                |--> wov_inaturalist_observations

wov_dictionary: standalone metadata lookup table
✨ Future Extensions
Table	Purpose
elog.wov_exports	Tracks what/when/where data was exported
elog.wov_sensor_context	Snapshot of underway data assoc. per obs
elog.wov_species_list	Voyage-specific watchlists, e.g., seabirds

Export to Sheets
📝 Licensing and Attribution Notes
Attribution metadata will be stored per observation/photo in license, user_id, user_login.

Export-layer formatting rules (Darwin Core, iNat CSV, eBird checklists) are designed as external templates and can map back to the tables described here.

Sensitive fields (e.g., private_latitude, geoprivacy) are retained but removed during open-data exports.

