<?php
if(!$_SESSION['login']){
    header('location:index.html');
    exit();
}
?>