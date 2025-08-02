# 📈 Entity Relationship Diagram — WoV Schema (v0.2.0)

> Generated: August 2025  
> Format: Mermaid ER Diagram (GitHub-compatible)  
> Location: `/docs/DATA_MODEL_ERD.md`

This diagram represents the core database structure used in the Wildlife Observation System (WoV) for RSV Nuyina.

erDiagram

wov_users ||--o{ wov_inaturalist_observations : "created_by"
wov_voyages ||--o{ wov_inaturalist_observations : "voyage_id"
wov_inaturalist_taxa ||--o{ wov_inaturalist_observations : "taxon_id"
wov_taxa ||--o{ wov_inaturalist_observations : "wov_taxa_id"
wov_inaturalist_taxa ||--o{ wov_taxa : "inaturalist_taxa_id"
wov_inaturalist_observations ||--o{ wov_images : "has images"

wov_users {
uuid user_id PK
text username
text email
text role
timestamp created_at
}

wov_voyages {
char(10) voyage_id PK
text name
date start_date
date end_date
text region
text notes
}

wov_inaturalist_taxa {
int inaturalist_taxa_id PK
text scientificname
text genus
text family
text kingdom
text taxonrank
}

wov_taxa {
int taxa_id PK
text original_name
text matched_name
text matched_canonical
text taxonomy_kingdom
text taxonomy_phylum
text taxonomy_class
text taxonomy_order
text taxonomy_family
text taxonomy_genus
int inaturalist_taxa_id FK
}

wov_inaturalist_observations {
int id PK
timestamp time_observed_at
double latitude
double longitude
int user_id FK
int wov_taxa_id FK
int taxon_id FK
char(10) voyage_id FK
text license
text image_url
}

wov_images {
uuid image_id PK
int observation_id FK
text file_path
timestamp datetime_original
}