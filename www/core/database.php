<?php

/**
* 
*/
class Database extends PDO
{
	
	public function __construct()
	{
		parent::__construct(DB_TYPE.':host='.DB_HOST.';port=3307;dbname='.DB_NAME, DB_USER, DB_PASS);
	}



    public function insert($table, $data)
    {
        ksort($data);
        
        $fieldNames = implode('`, `', array_keys($data));
        $fieldValues = ':' . implode(', :', array_keys($data));
    
        $sth = $this->prepare("INSERT INTO $table (`$fieldNames`) VALUES ($fieldValues)");
        
        foreach ($data as $key => $value) {
            $sth->bindValue(":$key", $value);
        }
        
        return $sth->execute();
    }

    public function login($username, $password){
        $sth = $this->prepare("SELECT uid FROM users WHERE 
                username = :username AND password = :password");
        $sth->execute(array(
            ':username' => $username,
            ':password' => $password
            ));
        return $data = $sth->fetch();
        

    }
    /**
     * select
     * @param string $sql An SQL string
     * @param array $array Paramters to bind
     * @param constant $fetchMode A PDO Fetch mode
     * @return mixed
     */
    public function select($sql, $array = array(), $fetchMode = PDO::FETCH_ASSOC)
    {
        $sth = $this->prepare($sql);
        
        /*foreach ($array as $key => $value) {
            $sth->bindValue("$key", $value);
        }*/

        $sth->execute();
        return $sth->fetchAll($fetchMode);
    }


    public function test1(){
    	$sqli = "j' OR ' 1=1";
        $sth = $this->prepare("SELECT id FROM users WHERE 
                login = 'henk' AND password = '$sqli'");
        print_r($sth);
        $sth->execute();
        /*$sth->execute(array(
            ':login' => "henks",
            ':password' => "henk"
        ));*/
        $data = $sth->fetch();
        print_r($data);

    }

 


}// einde class

?>