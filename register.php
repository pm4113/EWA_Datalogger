<?php
session_start();
if(isset($_SESSION["username"])) {
?>

<html>
</head>
	<!-- Required meta tags -->
    	<meta charset="utf-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    	<!-- Bootstrap CSS -->
    	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
<style>
table {
	border:1px solid black;
}
</style>
	<title>Admin Bereich</title>
	<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
	<div id="register">
	  <div id="registrieren">	
		<?php
		if(!isset($_GET["page"])) {
		?>
		<h4>Registrieren</h4>
		<table>
			<form action="register.php?page=2" method="post">
			<tr>
			<td align="right">Username:</td>		<td><input type="text" name="user" /><br /> </td>
			</tr>
			<tr>
			<td align="right">Passwort:</td>		<td><input type="password" name="pw" /><br /> </td>
			</tr>
			<tr>
			<td align="right">Passwort wiederholen:</td>	<td><input type="password" name="pw2" /><br /> </td>
			</tr>
			<tr>
			<td align="right">Zählernummer Leistung:</td>	<td><input type="text" name="power" /><br /> </td>
			</tr>
			<tr>
			<td align="right">Zählernummer Wasser:</td>	<td><input type="text" name="water" /><br /> </td>
			</tr>
			<tr>
			<td><input type="submit" value="Senden" /></td>
			</tr>
			</form>
		</table>
		<br />
		<?php
		}
		?>
	  </div>
	  <div id="passwort">	
		<!-- renew Passwort -->
		<?php
		if(!isset($_GET["page"])) {
		?>
		<h4>Passwort ändern</h4>
		<table>
			<form action="register.php?page=3" method="post">
			<tr>
			<td align="right">Username:</td>		<td><input type="text" name="user" /><br /> </td>
			</tr>
			<tr>
			<td align="right">Neues Passwort:</td>		<td><input type="password" name="pw" /><br /> </td>
			</tr>
			<tr>
			<td align="right">Neues Passwort wiederholen:</td>	<td><input type="password" name="pw2" /><br /> </td>
			</tr>
			<tr>
			<td><input type="submit" value="Senden" /></td>
			</tr>
			</form>
		</table>
		<br />
		<?php
		}
		?>
	  </div>


	  <div id="passwort">	
		<!-- renew Passwort -->
		<?php
		if(!isset($_GET["page"])) {
		?>
		<h4>Benutzer löschen</h4>
		<table>
			<form action="register.php?page=4" method="post">
			<tr>
			<td align="right">Username:</td>		<td><input type="text" name="user" /><br /> </td>
			</tr>
			<tr>
			<td><input type="submit" value="Senden" /></td>
			</tr>
			</form>
		</table>
		<br />
		<?php
		}
		?>
	  </div>


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
			
					if($eintrag and $usereintrag == true){
						echo "Vielen Dank. Du hast dich erfolgreich registriert... <a href=\"index.php\">Jetzt anmelden</a>";
					} else {
						echo "Fehler im System. Bitte versuche es später noch einmal...";
					}
					mysql_close($verbindung);
					}	
				}
			
			}
		}
		?>



		<?php
		if(isset($_GET["page"])) {
			if($_GET["page"] == "3") {
			$user = strtolower($_POST["user"]);
			$pw = md5($_POST["pw"]);
			$pw2 = md5($_POST["pw2"]);

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
				if($control == 0) {
					echo "Username nicht vorhanden. Bitte wähle einen anderen!! <a href=\"register.php\">zurück</a>";
				} else {
					$eintrag = "UPDATE tbl_userlogin SET passwort = '$pw' WHERE user = '$user'";
			
					$eintrag = mysql_query($eintrag);	
			
					if($eintrag == true){
						echo "Vielen Dank. Du hast das Passwort erfolgreich geändert... <a href=\"index.php\">Jetzt anmelden</a>";
					} else {
						echo "Fehler im System. Bitte versuche es später noch einmal...";
					}
					mysql_close($verbindung);
					}	
				}
			
			}
		}
		?>


		<?php
		if(isset($_GET["page"])) {
			if($_GET["page"] == "4") {
			$user = strtolower($_POST["user"]);

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
			if($control == 0) {
				echo "Username nicht vorhanden. Bitte wähle einen anderen!! <a href=\"register.php\">zurück</a>";
			} else {
				$loeschen_1 = "DELETE FROM tbl_userlogin WHERE user = '$user'";
			
				$loeschen_1 = mysql_query($loeschen_1);	
				mysql_select_db("datastorage")
				or die ("Verbindung zur Datenbank war nicht möglich...");
				$loeschen_2 =  "DROP TABLE $user";
				$loeschen_2 = mysql_query($loeschen_2);
				if(($loeschen_1 == true) and ($loeschen_2 == true)){
					echo "Sie haben einen Benutzer gelöscht... <a href=\"register.php\">zurück</a>";
				} else {
					echo "Fehler im System. Bitte versuche es später noch einmal...";
				}
				mysql_close($verbindung);
				}	
			}
				
		}
		?>


		  <div id="option">
		  <table>
			<form method="post" action="show_user.php">
			<tr>
				<td><input type="submit" value="Alle User anzeigen" /> </td>
			</form>
			<form method="post" action="logout.php">
				<td><input type="submit" value="Ausloggen" /> </td>
			</tr>
			</form>
		  </table>
		  </div>
	</div>
	<!-- Optional JavaScript -->
    	<!-- jQuery first, then Popper.js, then Bootstrap JS -->
    	<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
    	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
</body>
</html>

<?php
} else {
?>
Bitte erst einloggen, <a href="index.php">hier</a>.
<?php
}
?>
