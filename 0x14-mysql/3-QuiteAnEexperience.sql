-- Creates new user
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'password';
-- Grants needed permissions
GRANT ALL PRIVILEGES ON *.* TO 'replica_user'@'%';
