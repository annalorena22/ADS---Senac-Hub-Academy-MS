<?php
$host="localhost";
$usuario="root";
$senha="";
$bd="banco139";

$con=new mysqli($host,$usuario,$senha,$bd);

if ($con-> connect_errno){
    echo "Falha na Conexão:(".$con->connect_errno")".$con->connect_error;
}
else{
    echo "Conectado" . $con->host_info."\n";
}
?>