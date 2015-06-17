<?php
/*
*=======================================================================
*= 						olafelzinga index.php						   =
*=				for more info go to olaflelzinga.com 				   =
*=					Copyright olaf jwz niks van Dinesh		 		   =
*=======================================================================
*/
#################################################
# Default settings
#################################################
// error reporting #USE ONLY FOR TEST PURPOSES!!!
error_reporting(E_ALL);
ini_set('display_errors', 1);
session_start();
//Memory limit
ini_set('memory_limit', '100M');

//Tijdzone
date_default_timezone_set('Europe/Amsterdam');

#################################################
# default require
#################################################

foreach (glob("core/*.php") as $file)
{
	require $file;
}
require 'config.php';

#################################################
# start building register
#################################################
$register = new register;



#################################################
# load other core funtion and start router
#################################################

autoload('lib', True, $register);

$register->router = new router($register);

#################################################
# index funtions
#################################################

/**
* @param map
* @param declare True/False load class
* @param register for building register
*
*/
function autoload($map, $declare, $register){
	// foreach php file in folder
	foreach (glob($map."/*.php") as $file)
	{
		include $file;
		//if false don't load class
		if ($declare == True)
		{
			$filename = rtrim(trim($file, $map.'/'), ".php");
			$register->$filename = new $filename($register);
		}
	}
}

?>
