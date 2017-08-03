<?php
session_start();
if(isset($_SESSION["username"])) {
?>


<html>
	<head>
		<titel>Mein Bereich</titel>
	</head>
</html>


<?php
} else {
?>
Bitte erst einloggen, <a href="index.php">hier</a>
<?php
}
?>
