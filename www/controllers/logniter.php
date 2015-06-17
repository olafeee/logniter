<?php
class logniter extends baseController
{
	#public $model;
	#public $db;

	function __construct($register) {
		parent::__construct($register);
	}
	function pageviewspercountry($begin = '', $eind= ''){
		$data = array("startdate" => "01-01-2014", "enddate" => "31-12-2015");                                                                    
		$data_string = json_encode($data);                                                                                                                                                                                                                                                                                                                      
		
		$result = $this->apibellen('pageviewspercountry',$data_string);

		$this->register->pageviewspercountry = $result;
		$this->index('pageviewspercountry');
	}

	function clientstats(){
		$data = array("startdate" => "01-01-2014", "enddate" => "31-12-2015");                                                                    
		$data_string = json_encode($data);                                                                                  
		                                                                                                                     
        $result = $this->apibellen('clientstats',$data_string);
        
		$this->register->clientstats = $result;
		$this->index('clientstats');
	}

	function pageviews($period = "pageviewspermonth", $value = '2014'){
		print_r($period); 
		$data = array("year" => $value,);                                                                    
		$data_string = json_encode($data);

		                                                                                                                    
        $result = $this->apibellen($period, $data_string);
        print_r($result);
        
		$this->register->result = $result;
		$this->register->period = $period;
		$this->index('pageviews');
	}



	function apiBellen($endpoint_link,$data_string){
		$ch = curl_init('http://localhost:8080/'.$endpoint_link);                                                                      
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");                                                                     
		curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);                                                                  
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);                                                                      
		curl_setopt($ch, CURLOPT_HTTPHEADER, array(                                                                          
		    'Content-Type: application/json',                                                                                
		    'Content-Length: ' . strlen($data_string))                                                                       
		);                                                                                                                   
                                                                                                                    
		$result = curl_exec($ch);
		return $result;
	}

}