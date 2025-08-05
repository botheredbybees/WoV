# 📈 Entity Relationship Diagram — WoV Schema (v0.3.0)

> Generated: August 2025  
> Format: Mermaid ER Diagram (GitHub-compatible)  
> Location: `/docs/DATA_MODEL_ERD.md`

This diagram represents the core database structure used in the Wildlife Observation System (WoV) for RSV Nuyina.

erDiagram
    wov_users ||--o{ wov_observations : "created_by"
    wov_users ||--o{ wov_voyages : "manages"
    wov_voyages ||--o{ wov_observations : "has_voyage"
    wov_inaturalist_taxa ||--o{ wov_taxa : "inaturalist_match"
    wov_inaturalist_taxa ||--o{ wov_observations : "inaturalist_taxon"
    wov_inaturalist_taxa ||--o{ wov_inaturalist_observations : "inaturalist_taxon"
    wov_taxa ||--o{ wov_observations : "wov_taxon"
    wov_taxa ||--o{ wov_inaturalist_observations : "wov_taxon"
    wov_observations ||--o{ wov_images : "has_image"

    wov_dictionary {
        integer dictionary_id PK
        text parameter_or_variable
        text definition
        text units
    }

    wov_inaturalist_taxa {
        integer id PK
        integer inaturalist_taxa_id UK "Unique iNat ID"
        varchar scientificname
        varchar genus
        varchar family
        varchar kingdom
        varchar taxonrank
    }

    wov_taxa {
        integer taxa_id PK
        text original_name
        text matched_canonical
        integer inaturalist_taxa_id FK "wov_inaturalist_taxa.id"
        text taxonomy_kingdom
        text taxonomy_genus
    }

    wov_users {
        UUID user_id PK
        text username
        text email
        text role
    }

    wov_voyages {
        CHAR(10) voyage_id PK
        text name
        date start_date
        date end_date
    }

    wov_observations {
        integer observation_id PK
        UUID user_id FK "wov_users.user_id"
        CHAR(10) voyage_id FK "wov_voyages.voyage_id"
        integer wov_taxa_id FK "wov_taxa.taxa_id"
        integer taxon_id FK "wov_inaturalist_taxa.inaturalist_taxa_id"
        date observed_on
        float latitude
        float longitude
        text species_guess
        float sea_surface_temp
    }

    wov_inaturalist_observations {
        integer id PK
        date observed_on
        integer user_id "iNat user ID (no direct FK to wov_users)"
        integer taxon_id FK "wov_inaturalist_taxa.inaturalist_taxa_id"
        integer wov_taxa_id FK "wov_taxa.taxa_id"
        float latitude
        float longitude
        text scientific_name
    }

    wov_images {
        UUID image_id PK
        integer observation_id FK "wov_observations.observation_id"
        text file_path
        timestamp datetime_original
    }
