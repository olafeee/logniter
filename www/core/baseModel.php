<?php

class baseModel {

	protected $register;	

	function __construct($register)
	{
		$this->register = $register;
	}
    
	function connectDB(){
		$this->db = new Database();
	}

}