# Creates a file in /tmp.
file { 'school':
  ensure  => absent
  path    => './tmp/'
  content => 'I love Puppet'
  group   => 'www-data'
  mode    => '0744'
  owner   => 'www-data'
}
