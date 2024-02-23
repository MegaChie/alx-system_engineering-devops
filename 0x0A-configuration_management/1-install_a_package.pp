# Installs flask from pip3
exec { 'installing Flask package':
  command => 'pip install flask==2.1.0',
  path    => '/usr/bin/'
}
