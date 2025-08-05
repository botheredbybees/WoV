CREATE USER supabase_admin WITH PASSWORD 'excalibur';

GRANT ALL PRIVILEGES ON DATABASE wov TO supabase_admin;

-- Optionally, grant usage or privileges on schemas/tables as needed, e.g.
GRANT USAGE ON SCHEMA wov TO supabase_admin;
