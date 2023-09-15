/* put database initialization script here */

-- for example
CREATE ROLE djradmin WITH ENCRYPTED PASSWORD 'password' LOGIN;
COMMENT ON ROLE djradmin IS 'docker user for tests';

CREATE DATABASE djrdb OWNER djradmin;
COMMENT ON DATABASE djrdb IS 'docker db for tests owned by docker user';
