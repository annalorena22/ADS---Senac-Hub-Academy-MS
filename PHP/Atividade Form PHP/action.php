<?php
session_start();
include("connect.php")

if(empty($POST["nome"]) || empty ($POST["senha"])){
    header("location:index.php");
    exit();
}
?>