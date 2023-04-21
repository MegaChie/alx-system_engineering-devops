--- comment text
$file_place = "/tmp/school"
file { $file_place:
    ensure => "directory",
    owner => "www-data",
    group => "www-data",
    content => "I love Puppet",
    mode => 744
}
