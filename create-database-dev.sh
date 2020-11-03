#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER usr_prescription with password 'secret';
    CREATE DATABASE prescription_db;
    GRANT ALL PRIVILEGES ON DATABASE prescription_db TO usr_prescription;
EOSQL