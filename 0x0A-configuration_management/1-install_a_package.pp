# Installs flask from pip3
exec { 'flask installation':
  command  => 'pip install flask==2.0.1',
  provider => 'pip',
  path     => ['/usr/bin', '/usr/sbin']
}
