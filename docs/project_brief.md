Project Brief: Nuyina Wildlife Observation System
Objective:
Develop a shipboard web application for recording, managing, and sharing wildlife observations (birds, seals, whales, etc.) onboard the RSV Nuyina, integrating sensor-derived environmental context, enabling both real-time logging and professional photo uploads, and supporting eventual sync/export to international platforms such as iNaturalist.

Scope & Key Features:

Accessible web interface for all users (crew, scientists) across phones, tablets, and desktops

Local PostgreSQL storage for robust, offline-first operation and ample onboard data retention

Automated ingestion of ship sensor data via the underway data API—attaching environmental context to each observation with minimal user input

Flexible photo workflows: direct uploads (mobile) and batch uploads from pro cameras, auto-linked to underway context via EXIF datetime

Species identification support using locally cached iNaturalist images and, where possible, AI-based identification tools

Community-building features: group summaries, leaderboards, event logs, and review screens, fostering a sense of shared scientific purpose during voyages

Export/sync functionality to enable downstream sharing with the broader scientific/citizen science community (especially iNaturalist)

Extensibility for future data streams (sensor upgrades, acoustic, etc.)

Constraints:

Limited shipboard internet bandwidth; reliance on local resources is essential

Must integrate easily with AAD’s biodiversity database and underway data API

User experience must be intuitive for non-technical crew, but powerful for research staff