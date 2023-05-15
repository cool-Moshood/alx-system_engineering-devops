# fixing a webserver error returning error 500.

exec { 'fix the typographical error' :
command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.pp',
provider => shell
}

