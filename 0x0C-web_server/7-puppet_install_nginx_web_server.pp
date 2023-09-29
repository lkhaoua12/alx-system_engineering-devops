# Define a class for Nginx installation and configuration
class nginx_server {

  # Install Nginx package
  package { 'nginx':
    ensure => installed,
  }

  # Ensure Nginx service is enabled and running
  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  # Configure Nginx to listen on port 80
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    notify  => Service['nginx'],
  }

  # Create the root HTML page
  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    notify  => Service['nginx'],
  }

  # Create the 301 redirect for /redirect_me
  nginx::resource::location { 'redirect_me':
    location => '/redirect_me',
    content  => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  }

  # Reload Nginx whenever the configuration changes
  exec { 'nginx_reload':
    command     => '/usr/sbin/nginx -t && /usr/sbin/nginx -s reload',
    refreshonly => true,
    subscribe   => File['/etc/nginx/sites-available/default'],
  }
}

# Include the Nginx server class
include nginx_server

