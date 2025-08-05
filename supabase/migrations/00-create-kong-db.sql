CREATE USER supabase_admin WITH PASSWORD 'excalibur';
GRANT ALL PRIVILEGES ON DATABASE wov TO supabase_admin;
GRANT USAGE ON SCHEMA wov TO supabase_admin;

CREATE DATABASE kong;
