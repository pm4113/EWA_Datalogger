<?php
session_start();
$verhalten = 0;

if(!isset($_SESSION["username"]) and !isset($_GET["page"])) {
$verhalten = 0;
}
if($_GET["page"] == "log") {

$user = strtolower($_POST["user"]);
$passwort = md5($_POST["passwort"]);

$verbindung = mysql_connect("localhost", "ewa_datalogger", "ewaprojekt2017")
or die ("Fehler im System!");
mysql_select_db("userhandling")
or die ("Verbindung zur Datenbank war nicht möglich...");

$control = 0;
$abfrage = "SELECT * FROM tbl_userlogin WHERE user = '$user' AND passwort = '$passwort'";
$ergebnis = mysql_query($abfrage);
while($row = mysql_fetch_object($ergebnis))
	{
		$power = $row->power;
		$water = $row->water;
    		$control++;
     	}


if($control != 0) {
$_SESSION["username"] = $user;
$_SESSION["power"] = $power;
$_SESSION["water"] = $water;
$verhalten = 1;
} else {
$verhalten = 2;
}
}
?>

<html>
<head>
	<link rel="stylesheet" type="text/css" href="style.css" />
	<?php
	if($verhalten  == 1 and $user == "admin"){
	?>
		<meta http-equiv="refresh" content="3; URL=/data/register.php" />
	<?php
	} else if($verhalten  == 1){
	?>
		<meta http-equiv="refresh" content="3; URL=/data/datalogger.php" />
	<?php
	}
	?>
</head>
<body>
	<div id="register_1">
	<?php
	if($verhalten == 0) {
	?>
	Bitte loggen Sie sich ein:<br />
	<table>
	<form method="post" action="index.php?page=log">
		<tr>
		<td align="right">User:</td>		<td><input type="text" name="user" /><br/> </td>
		</tr>
		<tr>
		<td align="right">Passwort:</td>	<td><input type="password" name="passwort" /><br/> </td>
		</tr>
		<tr>
		<td><input type="submit" value="Einloggen" /> </td>
		</tr>
	</form>
	<?php
	}
	if($verhalten == 1) {
	?>
	Sie haben sich richtig eingeloggt und werden nun weitergeletet...
	<?php
	}
	if($verhalten == 2) {
	?>
	Falscher Username oder Passwort, <a href="index.php">zurück</a>.
	<?php
	}
	?>
	</div>
</body>
</html>
