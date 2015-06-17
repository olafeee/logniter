<?php

class logzunderModel extends baseModel{
	
	function __construct($register) {
		parent::__construct($register);
	}

    public function getInfo($day)
    {
    	$varr = $this->db->select('SELECT * FROM httpd_log.hour_pagehit WHERE datetime BETWEEN "2014-10-14 00:00:00" AND "2014-10-14 23:59:59"');
        return $varr;
    }

    function getUniqueVisitors(){
     	$var = $this->db->select('SELECT code,value,name FROM httpd_log.unique_visitors WHERE datetime BETWEEN "2014-11-15 00:00:00" AND "2014-11-18 23:59:59"');
        return $var;   	
    }




}
?>