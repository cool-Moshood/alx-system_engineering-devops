#Using Puppet, create a file in /tmp

file { '/tmp/school':
    ensure  => file,
    ownrer  => 'www-data',
    group   => 'www-data',
    mode    => '0744'
    content => 'I love Puppet'
}
