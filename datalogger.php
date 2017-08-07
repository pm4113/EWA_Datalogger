<?php
session_start();
if(isset($_SESSION["username"])) {
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
   <head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>EWA Datalogger</title>
	<link href="examples.css" rel="stylesheet" type="text/css">
	<!--[if lte IE 8]><script language="javascript" type="text/javascript" src="excanvas.min.js"></script><![endif]-->
	<script language="javascript" type="text/javascript" src="jquery.js"></script>
	<script language="javascript" type="text/javascript" src="jquery.flot.js"></script>
	<script language="javascript" type="text/javascript" src="jquery.flot.time.js"></script>
        <script language="javascript" type="text/javascript" src="jquery.flot.axislabels.js"></script>
	<script language="javascript" type="text/javascript" src="jquery.flot.navigate.js"></script>
	<script type="text/javascript">
	$(function(){ 
		//--------------------------php--------------------
                <?php
			$verbindung = mysql_connect("localhost", "ewa_datalogger", "ewaprojekt2017")
			or die ("Fehler im System");
			mysql_select_db("datastorage")
			or die ("Verbindung zur Datenbank nicht möglich");
                        $query = "SELECT * FROM (SELECT * FROM ".$_SESSION["username"]." ORDER BY date DESC LIMIT 100) sub ORDER BY date ASC";

			$results = mysql_query($query);
			$rows = array();
			while($row = mysql_fetch_array($results))
				$rows[] = $row;

                        foreach ($rows as $row) {
                        $points_1 .= "[" . $row['date'] . " , " . $row['waterflow'] . "] , ";
                        $points_2 .= "[" . $row['date'] . " , " . $row['power'] . "] , ";
                        }

                        $var_1 = "var datarecords_1 = [" . $points_1 . "];\n";
                        $var_2 = "var datarecords_2 = [" . $points_2 . "];\n";
			if ($row['waterflow']){
				$no_water_data = 0;
			} else {
				$no_water_data = 1;
			}

			if ($row['power']){
				$no_power_data = 0;
			} else {
				$no_power_data = 1;
			}
                        echo $var_1, $var_2, $no_water_data, $no_power_data;
                ?>
                //------------------------end php------------------

		<?php
		if (($no_water_data == 0) and ($no_power_data == 0)){
		?>
		var options = {
			lines: 	{	show: true},
			points:	{	show: true},
			grid:	{	hoverable: true},
			xaxis: {	ticks: 6,
					mode: "time",
					timezone: "browser",	
			    		timeformat: "%d.%m.-%H:%M"},
			yaxes:    	[{
					ticks: 8,
					position: "right",
					axisLabel: "Water Flow Rate [l/h]",
					axisLabelUseCanvas: true,
                			axisLabelFontSizePixels: 12,
                			axisLabelFontFamily: "Verdana, Arial, Helvetica, Tahoma, sans-serif",
                			axisLabelPadding: 5
					},{
					position: "left",
					axisLabel: "Power [W/h]",
					axisLabelUseCanvas: true,
               				axisLabelFontSizePixels: 12,
                			axisLabelFontFamily: "Verdana, Arial, Helvetica, Tahoma, sans-serif",
                			axisLabelPadding: 5
					}],
			legend: {	position: "nw"},
			zoom: {		interactive: true},
			pan: {		interactive: true}
	       			};

		//plot the graph
		var data = [
			{data: datarecords_1 , label: "Water Flow Rate [l/h]" , color: 6, yaxis:2},
			{data: datarecords_2 , label: "Power [W/h]" , color: 2}
			];
		$.plot("#placeholder", data, options);

		var overview = $.plot("#overview", [{data: datarecords_1, color:6, yaxis:2}, {data: datarecords_2, color: 2}], {
			series: {
				lines: {
					show: true,
					lineWidth: 1
				},
				shadowSize: 0
			},
			xaxis: {
				ticks: [],
				mode: "time"
			},
			yaxes: [{
				ticks: [],
				autoscaleMargin: 0.1,
                                position: "right",
                                axisLabel: "Water Flow Rate",
                                axisLabelUseCanvas: true,
                                axisLabelFontSizePixels: 12,
                                axisLabelFontFamily: "Verdana, Arial, Helvetica, Tahoma, sans-serif",
                                axisLabelPadding: 5
                                },{
				ticks: [],
				autoscaleMargin: 0.1,
                                position: "left",
                                axisLabel: "Power",
                                axisLabelUseCanvas: true,
                                axisLabelFontSizePixels: 12,
                                axisLabelFontFamily: "Verdana, Arial, Helvetica, Tahoma, sans-serif",
                                axisLabelPadding: 5
                                }]
		});
		
		<?php
		}
		?>


		<?php
		if (($no_water_data == 1) and ($no_power_data == 0)){
		?>
		var options = {
			lines: 	{	show: true},
			points:	{	show: true},
			grid:	{	hoverable: true},
			xaxis: {	ticks: 6,
					mode: "time",
					timezone: "browser",	
			    		timeformat: "%d.%m.-%H:%M"},
			yaxis:  {			
					position: "left",
					axisLabel: "Power [W/h]",
					axisLabelUseCanvas: true,
               				axisLabelFontSizePixels: 12,
                			axisLabelFontFamily: "Verdana, Arial, Helvetica, Tahoma, sans-serif",
                			axisLabelPadding: 5
					},
			legend: {	position: "nw"},
			zoom: {		interactive: true},
			pan: {		interactive: true}
	       			};

		//plot the graph
		var data = [
			{data: datarecords_2 , label: "Power [W/h]" , color: 2}
			];
		$.plot("#placeholder", data, options);

		var overview = $.plot("#overview", [{data: datarecords_2, color: 2}], {
			series: {
				lines: {
					show: true,
					lineWidth: 1
				},
				shadowSize: 0
			},
			xaxis: {
				ticks: [],
				mode: "time"
			},
			yaxis: { 
				ticks: [],
				autoscaleMargin: 0.1,
                                position: "left",
                                axisLabel: "Power",
                                axisLabelUseCanvas: true,
                                axisLabelFontSizePixels: 12,
                                axisLabelFontFamily: "Verdana, Arial, Helvetica, Tahoma, sans-serif",
                                axisLabelPadding: 5
                                }
		});
		
		<?php
		}
		?>


		<?php
		if (($no_water_data == 0) and ($no_power_data == 1)){
		?>
		var options = {
			lines: 	{	show: true},
			points:	{	show: true},
			grid:	{	hoverable: true},
			xaxis: {	ticks: 6,
					mode: "time",
					timezone: "browser",	
			    		timeformat: "%d.%m.-%H:%M"},
			yaxis:    	{
					ticks: 8,
					position: "left",
					axisLabel: "Water Flow Rate [l/h]",
					axisLabelUseCanvas: true,
                			axisLabelFontSizePixels: 12,
                			axisLabelFontFamily: "Verdana, Arial, Helvetica, Tahoma, sans-serif",
                			axisLabelPadding: 5
					},
			legend: {	position: "nw"},
			zoom: {		interactive: true},
			pan: {		interactive: true}
	       			};

		//plot the graph
		var data = [
			{data: datarecords_1 , label: "Water Flow Rate [l/h]" , color: 6}	
			];
		$.plot("#placeholder", data, options);

		var overview = $.plot("#overview", [{data: datarecords_1, color:6}], {
			series: {
				lines: {
					show: true,
					lineWidth: 1
				},
				shadowSize: 0
			},
			xaxis: {
				ticks: [],
				mode: "time"
			},
			yaxis: {
				ticks: [],
				autoscaleMargin: 0.1,
                                position: "left",
                                axisLabel: "Water Flow Rate",
                                axisLabelUseCanvas: true,
                                axisLabelFontSizePixels: 12,
                                axisLabelFontFamily: "Verdana, Arial, Helvetica, Tahoma, sans-serif",
                                axisLabelPadding: 5
                                }
		});
		
		<?php
		}
		?>
		
	});

	</script>
	<meta http-equiv="refresh" content = "1000">
   </head>
   <body>

	<div id="header">
		<h2>EWA Datalogger <?php echo $_SESSION["username"]?></h2>
	
	</div>

	<div id="content">

		<div class="demo-container">
			<div id="placeholder" class="demo-placeholder"></div>
		</div>

		<div class="demo-container" style ="height:150px">
                        <div id="overview" class="demo-placeholder"></div>
                </div>  

	</div>	

		<form method="post" action="logout.php">	
                	<input type="submit" value=" Abmelden" />		
        	</form>
	
	<div id="footer">
		BSc Markus Probst
	</div>

   </body>
</html>

<?php
} else {
?>
Bitte erst einloggen..., <a href="index.php">hier</a>.
<?php
}
?>
