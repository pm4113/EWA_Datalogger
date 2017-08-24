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
	<title>EWA Datalogger</title>
	<link rel="stylesheet" type="text/css" href="style.css" />

	<!-- Required meta tags -->
    	<meta charset="utf-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    	<!-- Bootstrap CSS -->
    	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">

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
	<?php
	if($verhalten == 0) {
	?>
	<div id="register">
	<h2>EWA Datalogger</h2>
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

	<!-- Optional JavaScript -->
    	<!-- jQuery first, then Popper.js, then Bootstrap JS -->
    	<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>

</body>
</html>
