# Install nginx
class { 'nginx': 
  ensure => 'installed',
}

# Configure nginx server
file { '/etc/nginx/sites-available/default':
  ensure => file,
  owner => 'root',
  group => 'root',
  content => template('nginx/default.erb'),
}

# Enable the nginx default site
file{ 'etc/nginx/sites-enables/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['Nginx'],
}

# Redirect Location
$redirect_location = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'

# 301 redirect
nginx::resource::location { 'redirect_me':
  ensure => present,
  location => {'redirect_me':
  rewrite => ['^/redirect_me$ $redirect_location permanent'],
  serve  => 'localhost',
  server_name => 'localhost',
  server_alias => ['localhost'],
  index_files => [],
  autoindex => 'off',
}  
