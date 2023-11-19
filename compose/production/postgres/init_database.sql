-- Archivo: 01_create_database.sql

DO $$
BEGIN
    RAISE NOTICE 'Creating database: %', current_setting('POSTGRES_DB');

    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = current_setting('POSTGRES_DB')) THEN
        EXECUTE 'CREATE DATABASE "' || current_setting('POSTGRES_DB') || '"';
        RAISE NOTICE 'Database created successfully.';
    ELSE
        RAISE NOTICE 'Database already exists.';
    END IF;
END $$;
