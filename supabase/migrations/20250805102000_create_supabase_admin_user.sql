-- Create supabase_admin user
DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE rolname = 'supabase_admin'
   ) THEN
      CREATE ROLE supabase_admin LOGIN PASSWORD 'excalibur';
   END IF;
END
$$;

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE wov TO supabase_admin;
GRANT USAGE ON SCHEMA wov TO supabase_admin;
