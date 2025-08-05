-- Create the wov schema if it does not exist
CREATE SCHEMA IF NOT EXISTS wov;

-- Create wov.wov_inaturalist_taxa_id_seq (assuming this exists or is also created)
CREATE SEQUENCE IF NOT EXISTS wov.wov_inaturalist_taxa_id_seq;

-- Create wov.wov_taxa_taxa_id_seq
CREATE SEQUENCE IF NOT EXISTS wov.wov_taxa_taxa_id_seq;

-- Grant connect and usage on your database and schema
-- (Adjust database name 'wov' if it's different in your .env)
GRANT CONNECT ON DATABASE postgres TO anon;
GRANT CONNECT ON DATABASE postgres TO authenticated;
GRANT CONNECT ON DATABASE postgres TO service_role;
GRANT CONNECT ON DATABASE postgres TO supabase_storage_admin;

-- Grant USAGE on the schema to Supabase roles
GRANT USAGE ON SCHEMA wov TO anon;
GRANT USAGE ON SCHEMA wov TO authenticated;
GRANT USAGE ON SCHEMA wov TO service_role;
GRANT USAGE ON SCHEMA wov TO supabase_storage_admin;

-- Grant SELECT privileges on all existing tables in 'wov' schema to 'anon'
-- This allows unauthenticated users to read data.
ALTER DEFAULT PRIVILEGES IN SCHEMA wov GRANT SELECT ON TABLES TO anon;
GRANT SELECT ON ALL TABLES IN SCHEMA wov TO anon;

-- Grant SELECT, INSERT, UPDATE, DELETE privileges on all existing tables in 'wov' schema to 'authenticated'
-- This allows logged-in users to perform CRUD operations.
ALTER DEFAULT PRIVILEGES IN SCHEMA wov GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO authenticated;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA wov TO authenticated;

-- Grant ALL PRIVILEGES on all existing tables in 'wov' schema to 'service_role'
-- This role is typically used by your backend services or admin functions and needs full control.
ALTER DEFAULT PRIVILEGES IN SCHEMA wov GRANT ALL PRIVILEGES ON TABLES TO service_role;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA wov TO service_role;


-- Grant USAGE and SELECT on sequences to 'authenticated' users for SERIAL/UUID columns
-- This ensures auto-incrementing IDs work for authenticated users when inserting new rows.
ALTER DEFAULT PRIVILEGES IN SCHEMA wov GRANT USAGE, SELECT ON SEQUENCES TO authenticated;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA wov TO authenticated;

-- Grant ALL PRIVILEGES on sequences to 'service_role'
ALTER DEFAULT PRIVILEGES IN SCHEMA wov GRANT ALL PRIVILEGES ON SEQUENCES TO service_role;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA wov TO service_role;

-- Create wov.wov_dictionary table
CREATE TABLE IF NOT EXISTS wov.wov_dictionary (
    dictionary_id SERIAL PRIMARY KEY,
    parameter_or_variable TEXT,
    definition TEXT,
    units TEXT,
    sampling_instrument TEXT,
    standard TEXT,
    csv_files TEXT
);

-- Create wov.wov_inaturalist_taxa table
CREATE TABLE IF NOT EXISTS wov.wov_inaturalist_taxa
(
    id SERIAL PRIMARY KEY, -- Changed to SERIAL PRIMARY KEY
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
    reference_url character varying COLLATE pg_catalog."default",
    inaturalist_taxa_id integer UNIQUE -- Simplified to a single UNIQUE constraint
);
CREATE INDEX IF NOT EXISTS idx_scientificname ON wov.wov_inaturalist_taxa (scientificname);
CREATE INDEX IF NOT EXISTS idx_taxa_id ON wov.wov_inaturalist_taxa (inaturalist_taxa_id);

-- Create wov.wov_taxa table
CREATE TABLE IF NOT EXISTS wov.wov_taxa (
    taxa_id integer NOT NULL DEFAULT nextval('wov.wov_taxa_taxa_id_seq'::regclass),
    original_name text COLLATE pg_catalog."default",
    matched_canonical text COLLATE pg_catalog."default",
    matched_name text COLLATE pg_catalog."default",
    source_key text COLLATE pg_catalog."default",
    current_name text COLLATE pg_catalog."default",
    current_canonical text COLLATE pg_catalog."default",
    synonym text COLLATE pg_catalog."default",
    data_source_id text COLLATE pg_catalog."default",
    data_source_title text COLLATE pg_catalog."default",
    current_classification_path text COLLATE pg_catalog."default", -- <<--- Ensure this is present
    joined_name text COLLATE pg_catalog."default",                -- <<--- Ensure this is present
    source text COLLATE pg_catalog."default",                     -- <<--- Ensure this is present
    level text COLLATE pg_catalog."default",                      -- <<--- Ensure this is present
    current_base_name text COLLATE pg_catalog."default",          -- <<--- Ensure this is present
    current_source text COLLATE pg_catalog."default",             -- <<--- Ensure this is present
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
        REFERENCES wov.wov_inaturalist_taxa (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

-- Create wov.wov_users table
CREATE TABLE IF NOT EXISTS wov.wov_users (
    user_id UUID PRIMARY KEY,
    username TEXT,
    role TEXT,
    email TEXT,
    created_at TIMESTAMP,
    inaturalist_id INTEGER, -- New column for iNaturalist user ID
    upload_to_inaturalist BOOLEAN DEFAULT FALSE, -- New column for iNaturalist upload preference
    upload_to_ebird BOOLEAN DEFAULT FALSE -- New column for eBird upload preference
);

-- Create wov.wov_voyages table (Planned)
CREATE TABLE IF NOT EXISTS wov.wov_voyages (
    voyage_id CHAR(10) PRIMARY KEY,
    name TEXT,
    start_date DATE,
    end_date DATE,
    region TEXT,
    notes TEXT
);

-- Table: wov.wov_inaturalist_observations

CREATE TABLE IF NOT EXISTS wov.wov_inaturalist_observations
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
        REFERENCES wov.wov_inaturalist_taxa (inaturalist_taxa_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT wov_taxa_fk FOREIGN KEY (wov_taxa_id)
        REFERENCES wov.wov_taxa (taxa_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

-- Create wov.wov_observations table for new observations
CREATE TABLE IF NOT EXISTS wov.wov_observations (
    observation_id SERIAL PRIMARY KEY, -- Primary key for this observation
    inaturalist_observation_id INTEGER, -- To store external iNaturalist observation ID if applicable
    observed_on DATE,
    time_observed_at TIMESTAMP,
    user_id UUID REFERENCES wov.wov_users(user_id), -- Foreign key to wov_users table
    user_login TEXT,
    species_guess TEXT,
    common_name TEXT,
    scientific_name TEXT,
    latitude FLOAT,
    longitude FLOAT,
    positional_accuracy INTEGER,
    wov_taxa_id INTEGER REFERENCES wov.wov_taxa(taxa_id),
    taxon_id INTEGER REFERENCES wov.wov_inaturalist_taxa(inaturalist_taxa_id),
    license TEXT,
    quality_grade TEXT,
    description TEXT,
    coordinates_obscured BOOLEAN,
    voyage_id CHAR(10) REFERENCES wov.wov_voyages(voyage_id),

    -- Additional fields for robust observations and underway data from dictionary
    sea_surface_temp FLOAT,
    wind_speed_true FLOAT, 
    wind_direction_true FLOAT, 
    air_temp FLOAT,
    salinity FLOAT,
    distance_to_animals FLOAT,
    group_size_estimate INTEGER,
    vessel_speed FLOAT,
    vessel_course FLOAT
);

-- Create wov.wov_images table (Planned)
CREATE TABLE IF NOT EXISTS wov.wov_images (
    image_id UUID PRIMARY KEY,
    observation_id INTEGER REFERENCES wov.wov_observations(observation_id), -- Updated FK reference to wov_observations
    file_path TEXT,
    camera_model TEXT,
    datetime_original TIMESTAMP,
    license TEXT
);