# kills a process named killmenow
exec {
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
