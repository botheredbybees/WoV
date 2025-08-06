\set pguser `echo "$POSTGRES_USER"`

CREATE DATABASE _supabase WITH OWNER :pguser;
CREATE DATABASE kong;
CREATE ROLE supabase_admin WITH LOGIN PASSWORD 'excalibur';
CREATE DATABASE wov OWNER supabase_admin;
CREATE ROLE anon NOLOGIN;
CREATE ROLE authenticated NOLOGIN;
CREATE ROLE service_role NOLOGIN;

