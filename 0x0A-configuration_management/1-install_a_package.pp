# Installs flask from pip3
package { 'installing Flask package':
  ensure   => '2.1.0',
  provider  => 'pip3',
  name     => 'Flask',
  install_options => 'installable'
}
