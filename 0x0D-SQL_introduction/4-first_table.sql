-- 4-first_table.sql
-- This script creates a table called first_table in the current database in your MySQL server
-- first_table description:
-- id INT
-- name VARCHAR(256)
-- If the table first_table already exists, the script does not fail
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
