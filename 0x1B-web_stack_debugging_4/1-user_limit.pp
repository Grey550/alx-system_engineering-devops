# Increase the hard and soft limit for the holberton user

exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/70000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/40000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
