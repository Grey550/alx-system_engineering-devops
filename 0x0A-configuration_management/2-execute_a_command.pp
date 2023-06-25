# Creating manifest that kills a process

exec { 'pkill':
  command   => '/usr/bin/pkill -f killmenow',
  provider  => 'shell',
}
