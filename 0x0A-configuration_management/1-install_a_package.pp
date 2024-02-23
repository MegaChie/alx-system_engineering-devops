# Installs flask from pip3, it will work on your machine, but not the checker
package { 'flask' :
  ensure   => '2.1.0',
  provider => 'pip3'
}
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
