# resolve the high number of failed request in other to handle 2000 requests to my server with 100 requests at a time
# using puppet i chenge the ULIMIT from 15 to 4096 which allows Nginx to handle a higher number of file descriptors

exec { 'update':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec { 'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}

