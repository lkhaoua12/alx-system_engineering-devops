# Define a package resource to install Flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Notify that the package is installed
notify { 'Flask installed':
  require => Package['Flask'],
}
