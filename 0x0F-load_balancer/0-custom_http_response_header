#!/usr/bin/env bash
# Comment text
apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
echo 'Hello World!' > /var/www/html/index.nginx-debian.html
sed -i '/server {/a add_header X-Served-By $hostname' /etc/nginx/sites-available/default
# "add_header X-Served-By $name" /etc/nginx/nginx.conf
service nginx start
