<?php
session_start();
if(isset($_SESSION["username"])) {
?>

<html>
<head>
<style>
table {
	border-collapse: collapse;
}
table,th,td{
	border: 1px solid black;
}
</style>
	<title>Daten aus einer Datenbank abrufen</title>
	<link rel="stylesheet" type="text/css" href="style.css" />
</head>
<body>
<?php
// Verbindung zum Datenbankserver
mysql_connect("localhost", "ewa_datalogger", "ewaprojekt2017") or die (mysql_error ());

// Datenbank auswählen
mysql_select_db("userhandling") or die(mysql_error());

// SQL-Query
$strSQL = "SELECT * FROM tbl_userlogin ORDER by user ASC";

// Query ausführen (die Datensatzgruppe $rs enthält das Ergebnis)
$rs = mysql_query($strSQL);
	
// Schleifendurchlauf durch $rs
// Jede Zeile wird zu einem Array ($row), mit mysql_fetch_array

echo '<div id="register_1">';
	echo "<table>";
	echo "<tr>";
                echo "<th><h3>User</h3></th>";
                echo "<th><h3>Stromzähler</h3></th>";
                echo "<th><h3>Wasserzähler</h3></th>";
	echo "</tr>";


	while($row = mysql_fetch_array($rs)) {
		// Schreibe den Wert der Spalte Vorname (der jetzt im Array $row ist
		echo "<tr>";
		echo "<td>".$row['user']."</td>";
		echo "<td>".$row['power']."</td>";
		echo "<td>".$row['water']. "</td>";
		echo "</tr>";
		}
	echo "<table>";
//echo '</div>'
// Schließt die Datenbankverbindung
mysql_close();
?>
<form method="post" action="register.php">
        <input type="submit" value="Zurück zur Userverwaltung" />
</form>

</body>
</html>

<?php
} else {
?>
Bitte erst einloggen, <a href="index.php">hier</a>.
<?php
}
?>
