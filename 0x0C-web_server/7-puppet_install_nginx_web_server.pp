#!/usr/bin/env bash
# comment text

apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
echo 'Hello World!' > /var/www/html/index.html
sed -i '/listen 80 default_server;/a rewrite ^/redirect_me https://youtu.be/PF5GBT9oJDo permanent;' /etc/nginx/sites-available/default
service nginx start
