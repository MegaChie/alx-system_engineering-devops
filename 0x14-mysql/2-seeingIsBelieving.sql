-- Creates a database
CREATE DATABASE IF NOT EXISTS tyrell_corp;
-- Add table with one entry
CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6 (id INT, name VARCHAR(256));
INSERT INTO tyrell_corp.nexus6 VALUES(2, 'MEGA');
