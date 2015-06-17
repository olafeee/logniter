<?php

class Router {

	#################################################
	# Constructor load url
	#################################################
	function __construct($register) {
		// laad url in 
		#$this->register->url = $register->parser->_urlParser();
		$url = $register->parser->_urlParser();
		//print_r($url);
		//echo"<br/>";
		// kijk of url doorgegevens word. als hij leeg is word index ingevuld
		if(empty($url[0])){
			require 'controllers/index.php';
			$controller = new Index($register);
			$controller->index('index');
			return false;
		}
		// de eerste deel van array vult hie hier in
		$file = 'controllers/' . $url[0] . '.php';

		//controller of file wel bestaad en daarna laat bijvoorbeeld controllers/index.php in
		if (file_exists($file)) {
			require $file;
		} else {
			$this->error($register);
			return false;
		}
		

		// laad class van desbetrefende contoller in
		$controller = new $url[0]($register);

		$urlLength = count($url);
		switch ($urlLength) {
			case '1':
				if (isset($url[0])) {
					$controller->index('index');
				} else {
				$this->error($register);
				//echo"doet het niet case 1";
				}
				break;
			case '2':
				if (method_exists($controller, $url[1])) {
					$controller->{$url[1]}('index');
				} else {
					$this->error($register);
				}
				break;
			case '3':
				if (method_exists($controller, $url[1])) {
					$controller->{$url[1]}($url[2]);
				} else {
					$this->error($register);
				}
				break;
			case '4':
				if (method_exists($controller, $url[1])) {
					$controller->{$url[1]}($url[2],$url[3]);
				} else {
					$this->error($register);
				}
				break;
			default:
				$controller->index('index');
				break;
		}//eind switch
	}// end construtopr

	#################################################
	# error page
	#################################################
	function error($register) 
	{
		require 'controllers/error.php';
		$controller = new Error($register);
		$controller->index('index');
		return false;
	}
}                                                             