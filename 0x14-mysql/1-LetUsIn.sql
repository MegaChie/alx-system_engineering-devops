-- Creates said user with said password
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
-- Grants needed permissions
GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost';

