<?php

class baseView {

	private $register;
	private $vars = array();
	
	function __construct($register)
	{
		$this->register = $register;
		//echo $this->register->test;
	}

	public function __set($index, $value)
	 {
			$this->vars[$index] = $value;
	 }

	/**
	* render laad de header container en de footer
	* @param string $name is folder/pagina
	*/
	public function render($name){
		// Load variables
		foreach ($this->vars as $key => $value)
		{
			$$key = $value;
		}			
		require 'views/header.php';
		require 'views/' . $name . '.php';
		require 'views/footer.php';	
	}
	
	public function renderBlank($name){
		// Load variables
		foreach ($this->vars as $key => $value)
		{
			$$key = $value;
		}		
		require 'views/' . $name . '.php';	
	}
}