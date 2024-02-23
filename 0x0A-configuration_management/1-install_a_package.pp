# Installs flask from pip3
exec { 'installing Flask package':
  command => 'pip3 install Flask == 1.2.0',
  path    => '/usr/bin/'
}
