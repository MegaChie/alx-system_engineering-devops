# Installs flask from pip3
package { 'installing Flask package':
  ensure   => '2.1.0',
  name     => 'Flask',
  provider  => pip3
}
