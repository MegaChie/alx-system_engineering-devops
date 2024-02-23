# Creates a file in /tmp.
$filepath = '/tmp/school'
file { $filepath:
  ensure  => 'file'
  content => 'I love Puppet'
  group   => 'www-data'
  mode    => '0744'
  owner   => 'www-data'
}
