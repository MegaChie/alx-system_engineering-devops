# Installs flask from pip3, it will work on your machine, but not the checker
exec { 'flask installation':
  command => 'pip install flask==2.0.1',
  path    => '/usr/bin/pip'
}
