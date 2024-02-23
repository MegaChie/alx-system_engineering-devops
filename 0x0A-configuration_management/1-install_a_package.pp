# Installs flask from pip3
exec { 'flask installation':
  command => 'pip3 install flask==2.0.1',
  path    => '/usr/bin/pip3'
}
