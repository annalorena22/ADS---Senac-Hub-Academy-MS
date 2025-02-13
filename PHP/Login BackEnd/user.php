<?php
 
session_start();
include("verificacao.php");
 
if($_SESSION['setor']!='admin'){
    header("location: index.html");
    exit();
};
 
?>
 
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastrar Cliente</title>
</head>
<body>
    <h1>Cadastrar Cliente</h1>
   
    <h5><?php
    echo "login = ".$_SESSION['login']."<br>";
    echo "setor = ".$_SESSION['setor']."<br>";
    ?></h5>
 
    <form method= "POST" action="action_user.php">
        Nome <input type="text" name="first_name" id="fn">
        Sobrenome <input type="text" name="last_name" id="ln">
        Fone <input type="text" name="fone" id="fone">
        Endereço <input type="text" name="address" id="add">
        Email <input type="text" name="email" id="email">
        Sexo <input type="text" name="sexo" id="sexo">
        <input type="submit" name="sub" id="">
    </form>
   
    <a href="logout.php">Sair</a>
</body>
</html>
 