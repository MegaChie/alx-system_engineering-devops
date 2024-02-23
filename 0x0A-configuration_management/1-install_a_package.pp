# Creates a file in /tmp.
file { 'installing Flask':
  ensure => '2.1.0',
  name => 'Flask',
  provider => 'pip'
}
