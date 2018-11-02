<?php
if(isset($_GET['page'])){
	$ip = $_SERVER['REMOTE_ADDR'];
	$ua = $_SERVER['HTTP_USER_AGENT'];
	$date = date('l jS \of F Y h:i:s A');
	$w = $ip."||".$ua."||".$date;
	$file = fopen("prueba-01.txt", "a+");
	fwrite($file, $w . PHP_EOL);
	fclose($file);
	header('Location: http://www.quantika14.com/');
}else{
	header('Location: http://www.quantika14.com');
}
?>
