# Creates a file in /tmp.
file { "school":
  path => "./tmp/"
  ensure => absent
  content => "I love Puppet"
  group => "www-data"
  mode => 0744
  owner => "www-data"
}
