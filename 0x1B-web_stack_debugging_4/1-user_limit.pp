# This script enables the holberton user to login and open files without errors

exec { 'OS-security-configuration' :
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}
