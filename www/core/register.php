<?php
Class Register {
     public $vars = array();


    /**************************************************
    *  Var setter
    **************************************************/
     public function __set($index, $value)
     {
        $this->vars[$index] = $value;
     }

    /**************************************************
    *  Var getter
    **************************************************/
     public function __get($index)
     {
        if(isset($this->vars[$index])){
             return $this->vars[$index];
        }
     }

    public function __isset($var) { 
        return isset($this->vars[$var]); 
    } 
     
    public function __unset($var) { 
        unset($this->vars[$var]); 
    } 

}
?>