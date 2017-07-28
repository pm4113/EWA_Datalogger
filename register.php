<html>
</head>
	<title>Mein Bereich - Registrieren</title>
</head>
<body>
<h3>Registrieren</h3>
<?php
if(!isset($_GET["page"])) {
?>
	<form action="register.php?page=2" method="post">
	Username:		<input type="text" name="user" /><br />
	Passwort:		<input type="password" name="pw" /><br />
	Passwort wiederholen:	<input type="password" name="pw2" /><br />
	Zählernummer Leistung:	<input type="text" name="power" /><br />
	Zählernummer Wasser:	<input type="text" name="water" /><br />
	<input type="submit" value="Senden" />
	</form>
<?php
}
?>
<?php
if(isset($_GET["page"])) {
	if($_GET["page"] == "2") {
	$user = strtolower($_POST["user"]);
	$pw = md5($_POST["pw"]);
	$pw2 = md5($_POST["pw2"]);
	$power = $_POST["power"];
	$water = $_POST["water"];	

	if($pw != $pw2){
		echo "Die eingegebenen Passwörter stimmen nicht überein. Bitte wiederhole deine Eingabe! <a href=\"register.php\">zurück</a>";
	} else {
		$verbindung = mysql_connect("localhost", "ewa_datalogger", "ewaprojekt2017")
		or die ("Fehler im System!");
		mysql_select_db("userhandling")
		or die ("Verbindung zur Datenbank war nicht möglich...");	

		$control = 0;
		$abfrage = "SELECT user FROM tbl_userlogin WHERE user = '$user'";
		$ergebnis = mysql_query($abfrage);
		while($row = mysql_fetch_object($ergebnis))
			{
				$control++;
			}
		if($control != 0) {
			echo "Username schon verbeben. Bitte wähle einen anderen!! <a href=\"register.php\">zurück</a>";
		} else {
			$eintrag = "INSERT INTO tbl_userlogin
			(user, passwort, power, water)

			VALUES
			('$user', '$pw', '$power', '$water')";
			
			$eintrag = mysql_query($eintrag);
			
			mysql_select_db("datastorage")
			or die ("Verbindung zur Datenbank war nicht möglich");	
			
			$usereintrag = "CREATE TABLE ".$user." (
					id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
					date TEXT,
					waterflow INT(11),
					power INT(11)
					)";
			
			$usereintrag = mysql_query($usereintrag);
			
			if($eintrag == true){
				echo "Vielen Dank. Du hast dich erfolgreich registriert... <a href=\"index.php\">Jetzt anmelden</a>";
			} else {
				echo "Fehler im System. Bitte versuche es später noch einmal...";
			}
			if($usereintrag == true){
				echo "Vielen Dank. Es hat funktioniert...";
			} else {
				echo "Fehler im System. Bitte versuche es später noch einmal...";
			}
			mysql_close($verbindung);
			}	
		}
			
	}
}
?>
</body>
</html>
