# comment text
exec { 'killer':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
}
