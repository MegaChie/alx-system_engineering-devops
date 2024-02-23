# Creates a file in /tmp.
package { 'installing Flask':
  ensure   => '2.1.0',
  name     => 'Flask'
  provider => 'pip'
}
