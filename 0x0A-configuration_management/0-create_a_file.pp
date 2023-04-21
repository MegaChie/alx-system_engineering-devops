--- comment text
$filePlace = "/tmp/school"
file { $filePlace:
	ensure => "directory",
	owner => "www-data",
	group => "www-data",
	content => "I love Puppet",
	mode => 0744
}
