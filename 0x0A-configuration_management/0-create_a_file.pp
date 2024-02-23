# Creates a file in /tmp.
$filePath = '/tmp/school'
file { $filePath:
  ensure  => 'file'
  content => 'I love Puppet'
  group   => 'www-data'
  mode    => '0744'
  owner   => 'www-data'
}
