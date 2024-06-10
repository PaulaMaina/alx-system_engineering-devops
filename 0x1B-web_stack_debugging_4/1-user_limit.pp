# This script enables the holberton user to login and open files without errors

exec { 'increase-hard-file-limit-for-the-holberton-user' :
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
} ->

exec { 'increase-soft-file-limit-for-the-holberton-user':
  command => 'sed -i "/holberton soft/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}