🚀 WoV Project Delivery Timeline
Last updated: 2025-08-05
Time Zone: AEST
Notation: Each sprint = 2 weeks by default. Adjust dates or sprint durations as your team prefers.

Sprint 0: Foundation (Prep & Onboarding) — 2025-08-04 → 2025-08-15
[x] Repository and documentation structure established.

[x] Base Supabase/FastAPI Docker Compose stack runs locally (docker compose up).

[x] Developer setup guide /docs/SETUP_ENVIRONMENT.md.

[x] .env.example finalized, secrets not committed.

[x] Initial data dictionary and ERD mermaid structure in /docs.

Sprint 1: Core Schema & Authentication — 2025-08-18 → 2025-08-29
[x] Taxa, observations, dictionary tables implemented and indexed.

[x] User table structure added and RLS/role placeholders defined.

[x] Supabase Auth (GoTrue) integration via Docker Compose.

[x] Voyage tracking table and observation/voyage linkage.

[x] Developer access to Supabase Studio and database meta interface.

[x] Initial data loaded into wov_inaturalist_taxa, wov_taxa, wov_inaturalist_observations, wov_dictionary.

Sprint 2: iNaturalist Image Integration & Basic Data Flow — 2025-09-01 → 2025-09-12
[ ] Implement iNaturalist Image Fetching: Develop a mechanism (e.g., FastAPI endpoint or background worker) to pull images from the iNaturalist API based on inaturalist_observation_id and store/cache them locally in Supabase Storage.

[ ] Update wov_images table: Ensure it can store references to these locally cached iNaturalist images.

[ ] FastAPI service up with /observations, /taxa, /voyages endpoints.

[ ] Demo pipeline: add observation, auto-link to taxa, voyage, and user.

[ ] Add mock/test InfluxDB and (optional) minimal underway sensor API integration.

[ ] Populate seed/sample data: taxa, voyages, users, observations.

Sprint 3: Export & Interop — 2025-09-15 → 2025-09-26
[ ] Views/functions for:

Darwin Core (ALA) CSV [docs/export-templates/ALA_DarwinCore_template.csv]

iNaturalist CSV [docs/export-templates/iNaturalist_CSV_example.csv]

eBird checklists [docs/export-templates/eBird_checklist_template.csv]

[ ] Enable CSV/PostgREST view-based HTTP export endpoints.

[ ] First field-test export (manual or automated) for ALA/iNat trial upload.

Sprint 4: Web UI Form Prototypes — 2025-09-29 → 2025-10-10
[ ] Minimal SvelteKit frontend enables:

Log new observation (species, count, notes, photos)

Choose voyage and user

Preview map and list of all observations

[ ] Basic mobile-first UI layout scaffold

[ ] Image upload + Supabase Storage proof-of-concept

Sprint 5: Enrichment & Validation — 2025-10-13 → 2025-10-24
[ ] Offline observation creation and sync (PWA shell or explicit local queue)

[ ] Taxon name validation and autocomplete (from wov_taxa)

[ ] Add sensor context: link observations to nearest underway record (using test/mock data)

[ ] Structured photo EXIF parsing and auto-matching to sensor data

Sprint 6: Security, RLS, and Access Control — 2025-10-27 → 2025-11-07
[ ] Add and enforce Row-Level Security in Supabase for:

Role-based access (crew/scientist/admin)

Voyage/user data partitioning

[ ] Audit observation creation to ensure only authenticated users can insert/modify/delete

[ ] Disable direct API access except via JWT/GoTrue or admin

Sprint 7: Dashboard, Review & Reporting — 2025-11-10 → 2025-11-21
[ ] Voyage summaries and per-species dashboards (SvelteKit/Studio)

[ ] Review/verification queue for ‘admin’/‘lead scientist’ role

[ ] Field/shipboard daily log and summary export features

[ ] Integrated gallery and media viewer (photos per taxon/etc.)

Sprint 8: Documentation, Packaging & Field Test — 2025-11-24 → 2025-12-05
[ ] User documentation and operations guide

[ ] Onboard/offboard Docker Compose (single script/command)

[ ] Export/backup all project data (schema, env, redacted data exports)

[ ] Shipboard field-test with real observations, offline and online

Post-Launch/”Blue Sky” / Optional Sprints
[ ] Machine Learning: On-device/species-suggestion (low priority, stretch)

[ ] QR code/shortlink integration for photo-attribution on ship devices

[ ] Live map/heatmap visualization with sensor overlays

[ ] Interop with AADC/iNaturalist/ALA APIs for live sync or bulk push

[ ] Discussions/comments/reputation for observations (community inspired)

[ ] Field experiment: Android/iOS PWA packaging and photo capture UX

🚩 Standing Suggestions
At the end of each sprint: review backlog, triage bugs, demo to data users.

Prioritize documentation, reproducibility, and audit trails.

Field-test real world workflows on real ship computers at the earliest opportunity.

Sprint planning is flexible:
If you need to split, combine, or reschedule, update this file or file an issue on the repo