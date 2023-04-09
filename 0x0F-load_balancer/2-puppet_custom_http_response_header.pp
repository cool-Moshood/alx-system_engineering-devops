# Automate the task of creating a custom HHTP header respond with puppet

$file_content="
server {
	listen 80 default_server;
	add_header X-Served-By ${hostname};
	root /var/www/html;
	index index.html;
	error_page 404 /404.html;
	location = /404.html {
		internal;
	}
	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}
}
"

package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

file {'/var/www/html/index.html':
ensure  => file,
content => 'Hello World!
',
require => Package['nginx']
}

file {'/var/www/html/404.html':
ensure  => file,
content => "Ceci n'est pas une page
",
require => File['/var/www/html/index.html']
}

file {'/etc/nginx/sites-enabled/default':
ensure  => file,
content => $file_content,
require => File['/var/www/html/404.html']
}

exec {'nginx-restart':
command  => 'service nginx restart',
provider => 'shell',
require  => File['/etc/nginx/sites-enabled/default']
}

