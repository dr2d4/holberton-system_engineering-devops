# Puppet configuration
exec { 'config_server':
  provider => shell,
  command  => 'sudo apt update; sudo apt -y install nginx; echo "Holberton School" | sudo tee /var/www/html/index.html; new_string="server_name _;\n\trewrite ^\/redirect_me http:\/\/dr2d4.tech\/ permanent;"; sudo sed -i "s/server_name _;/$new_string/" /etc/nginx/sites-available/default; sudo nginx -t; sudo service nginx restart',
  }
