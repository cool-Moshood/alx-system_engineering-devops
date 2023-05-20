# resolve problem of high number of opened file by update the limits.conf file and replace the line that specifies the maximum number of file descriptors

exec { 'update-1':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',
  before   => Exec['update-2'],
}

exec { 'update-2':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',
}
