# kills a process named killmenow
exec { 'a killing puppet script':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
