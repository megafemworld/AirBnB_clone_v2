#!/usr/bin/env bash
#  Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo -p /data/web_static/shared data/web_static/releases/test
echo "<html>
  <head>
  </head>
  <body>
    Server setup
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR unbuntu:unbuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\talis /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
