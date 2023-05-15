# fixing a webserver error returning error 500.

excute { 'fix the typographical error' :
	command => 'sed -i "s/phpp/php/g" /var/www/html/wp-setting.pp',
	provider => shell
	}
