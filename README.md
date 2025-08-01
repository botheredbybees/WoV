# 🐧 Nuyina Wildlife Observation System

📦 Version: 0.2.0
📅 Status: In Planning
🌐 License: Creative Commons Attribution (CC BY 4.0) (recommend revisiting at launch)

## 🚢 Overview

This project documents the planning and development of a shipboard biodiversity logging platform for the RSV Nuyina.

The system is designed to support:

- Casual expeditioner wildlife sightings (e.g., seabirds, whales, seals)
- Structured ecological surveys (e.g., pelagic bird transects)
- Integration with automated environmental context (via the InfluxDB-based underway data API)
- Seamless and license-aware export to iNaturalist, ALA, and other biodiversity platforms


## 🌟 Key Goals

- 🖥️ Cross-device web app for logging, reviewing, and exporting onboard wildlife observations.
- 📶 Offline-first operation with a fully local backend (Docker + Supabase + FastAPI).
- 📸 Image annotation and EXIF-based data linking for professional photo uploads.
- 🔁 Modular export support: ALA (Darwin Core), iNaturalist, eBird, BioCollect.
- 🗳️ Group participation \& engagement: voting, summaries, “photo of the voyage.”
- 🔐 Rich attribution + licensing metadata integrated at all levels.


## 👥 Audience

- Casual users (expeditioner photographers, general crew)
- Scientific observers conducting structured protocols
- Data management/admin teams
- External data consumers: iNaturalist, ALA, AAD


## 🛠️ Technology Stack

| Layer | Tool(s) |
| :-- | :-- |
| Frontend | SvelteKit / Vue 3 (touch \& offline-friendly) |
| Backend | FastAPI (Python), Dockerized |
| Auth + Storage | Supabase (PostgreSQL, Auth, Storage + Studio) |
| Sensor Data | InfluxDB (underway data, containerized restore) |
| Image Viewer | HTML-based, zoomable image reference guide |

## 📁 Repository Structure (Planned)

```
/
├── README.md
├── docs/
│   ├── NuyinaWildlifeObservationSystem_v0.2.0.md
│   └── export-templates/
│       ├── iNaturalist_CSV_example.csv
│       ├── eBird_checklist_template.csv
│       └── ALA_DarwinCore_template.csv
├── backend/
│   └── fastapi/
├── docker/
│   ├── docker-compose.yml
│   └── .env.example
└── .gitignore
```


## 📦 Getting Started (Planning Phase)

1. Clone the repository:

```bash
git clone https://github.com/YOUR_ORG/nuyina-wildlife-observation.git
cd nuyina-wildlife-observation
```

2. Review planning docs in the /docs folder:
    - ✅ Project scope \& spec
    - 🧩 Export schema plans
3. (Optional) Run the stack (when ready for dev):

```bash
docker compose up --build
```

4. Share feedback via GitHub Issues or Discussions

## 📄 Documentation Index

- 📘 [System Design (v0.2.0)](docs/NuyinaWildlifeObservationSystem_v0.2.0.md)
- 📤 Export Templates — Coming soon


## 🤝 Contributions

Planning is collaborative! Feel free to open:

- Ideas and enhancements
- Structured export examples
- Documentation PRs


## 📝 License \& Attribution

Field observations and photos will be optionally released under researcher-chosen licenses (CC-BY / CC0 where possible). The platform's code will be MIT or similar.

Data sharing is designed to comply with ALA and iNaturalist rules around attribution, consent, and licensing.
