<!-- php 1  -->
 
<?php
 
$variavel = $_GET["nome"];
echo "O nome digitado foi $variavel <br>";
 
?>

<!-- php 2  -->
 
 
<?php
 
$sistema = $_POST["sistema"];
echo "O Sistema operacional selecionado foi $sistema <br>";
 
?>

<!-- php 3  -->
 
 
<?php
 
$opcao = $_POST["option"];
 
for ($i=0; $i<count($opcao);$i++) {
echo "A opção selecionada foi $opcao[$i] <br>";
}
?>