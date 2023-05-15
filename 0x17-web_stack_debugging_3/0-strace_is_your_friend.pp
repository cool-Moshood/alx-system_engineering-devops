# fixing a webserver error returning error 500.

exec { 'Fix the typo':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => shell
}

