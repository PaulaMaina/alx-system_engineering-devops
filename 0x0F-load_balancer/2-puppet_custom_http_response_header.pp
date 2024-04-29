# Custom HTTP header response script
exec { 'update':
  command  => 'sudo apt -y update',
  provider => shell,
}
-> package {'nginx': 
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  line     => "location / {
  add_header X-Server-By ${HOSTNAME};",
  match    => '^\tlocation / }',
}
-> exec { 'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
