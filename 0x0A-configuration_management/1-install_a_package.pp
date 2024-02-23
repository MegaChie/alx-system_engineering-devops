# Installs flask from pip3
exec { 'flask installation':
  command  => 'pip3 install flask==2.0.1',
  provider => 'pip3',
  path     => ['/usr/bin', '/usr/sbin']
}
