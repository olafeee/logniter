<?php
abstract class baseController {

	protected $register;

	function __construct($register)
	{
		$this->register = $register;
		$this->register->baseView = new baseView($register);
		$this->url = $this->register->parser->_urlParser();
		$this->register->baseView->url = $this->url;	
	}


	/**
     * index
     * @param string $value welke pagina geladen moet worden 
     */
	function index($value, $blankPage = FALSE) {

		$url = $this->url;

		if (isset($value)){
			$pagina = $value;
		}else{
			$pagina = 'index';
		}

		//als er geen url is opgegeven vul rul in
		if(empty($url[0])){
			$url[0]='index';
		}

		// Laad view in al die er is
		$file = 'views/' . $url[0] . '/index.php';
		
		if (isset($url[1])) {
			$file = 'views/' . $url[0] .'/'. $url[1].'.php';
		}
		if (file_exists($file)) {
			$map = $url[0];
		}else{
			$map = 'error';
			$pagina ='index';
		}

		if ($blankPage == TRUE) {
			$this->register->baseView->renderBlank($map.'/'.$pagina);
		} else {
			$this->register->baseView->render($map.'/'.$pagina);
		}
		

	}

	/**
     * laadModel laad model in
     */
	function laadModel($register){
		$url = $this->url;
		if(empty($url[0])){
			$url[0] = "index";
		}
		$file = $url[0].'Model';
		$dir_file = 'models/'.$file.'.php';
		if(file_exists($dir_file)){
			require $dir_file;
			$model = new $file($register);
			return $model;
		}
	}

	/*
     * matchInt kijk of alleen cijfers is 
     * @param string $number is cijfer dat gechecked wordt
     *
	function matchInt($number){
	    if (preg_match('/^[0-9]{1,}$/', $number)) {
	    	return $number;
		}
	}	*/
}
