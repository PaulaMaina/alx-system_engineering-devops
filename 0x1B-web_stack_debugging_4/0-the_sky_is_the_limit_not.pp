# This script increases the amount of traffic an NGINX server can handle
exec { 'fix-nginx' :
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}
