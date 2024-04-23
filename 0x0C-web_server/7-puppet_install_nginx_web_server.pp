# Installs and configures an nginx web server

exec { 'install':
  provider => 'shell',
  command  => 'sudo apt -y update ; sudo apt -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me htpps:\/\/www.youtube.com\/watch?v=QH2-TGUIwu4 permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
