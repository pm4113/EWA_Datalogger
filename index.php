<?php
session_start();
$verhalten = 0;

if(!isset($_SESSEION["username"]) and !isset(?_GET["page"])) {
$verhalten = 0;
}
if($_GET["page"] == "log") {

$user = $_POST["user"];
$passwort = $_POST["passwort"];

if($user == "Markus" and $passwort == "toll") {
$_SESSEION["username"] = $user;
$verhalten = 1;
} else {
$verhalten = 2;
}
}
?>

<html>
<head>
	<titel>Login</titel>
	<?php
	if($verhalten  == 1){
	?>
		<meta http-equiv="refresh" content="3; URL=datalogger.php" />
	<?php
	}
	?>
</head>
<body>
	<?php
	if($verhalten == 0) {
	?>
	Bitte logge dich ein:<br />
	<form method="post" action="index.php?page=log">
		User:<input type="text" name="user" /><br/>
		Passwort:<input type="password" name="passwort" /><br/>
		<input type="submit" value="Einloggen" />
	</form>
	<?php
	}
	if($verhalten == 1) {
	?>
	Du hast dich richtig eingeloggt und wirst nun weitergeleitet!
	<?php
	}
	if($verhalten == 2) {
	?>
	Falscher Username oder Passwort, <a href="index.php">zurück</a>.
	<?php
	}
	?>
</body>
</html>
