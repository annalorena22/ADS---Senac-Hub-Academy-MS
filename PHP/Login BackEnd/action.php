<?php
session_start();
include("conn.php");
$login = mysqli_real_escape_string($con, $_POST["login"]);

$senha = mysqli_real_escape_string($con, $_POST["senha"]);

if (empty($login) || empty($senha)) {
    echo "<script>
            alert('Por favor, preencha todos os campos.');
            setTimeout(function(){
                window.location.href = 'login.php';
            }, 10000); // Espera 2 segundos antes de redirecionar
          </script>";
    exit(); 
}

$query = "select * from user where login = '{$login}' and senha = '{$senha}' ";

$result= mysqli_query($con, $query);


$row = mysqli_num_rows($result);
$retorno = mysqli_fetch_array($result);

if ($row>0){
    $_SESSION["login"] = $login;
    // header("location:admin.php");
    $_SESSION["setor"] = $retorno['setor'];

    if ($_SESSION['setor'] == 'admin'){
        header('location:admin.php');
    }
    else if ($_SESSION['setor'] == 'comum'){
        header('location:user.php');
    }
    if ($_SESSION['setor'] != 'admin'){
        header('location:index.html');
    }

    exit();
}

?>
