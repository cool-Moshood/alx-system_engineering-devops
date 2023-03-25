# Using Puppet, create a file in /tmp.

file { '/tmp/school':
    ownrer  => 'www-data',
    group   => 'www-data',
    mode    => '0744'
    content => 'I love Puppet'
}
