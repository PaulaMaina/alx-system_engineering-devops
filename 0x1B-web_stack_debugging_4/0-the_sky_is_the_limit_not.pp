# This script increases the amount of traffic an NGINX server can handle
exec { 'fix--for-nginx' :
  command => 'sed -i "s/15/2000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
