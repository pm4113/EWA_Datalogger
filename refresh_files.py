import xml.etree.ElementTree as ET
import datetime
import string
import MySQLdb
from pdb import set_trace as bp


begin_time = 0
end_time = 0
debug = False

def time_update():
	global begin_time
	global end_time
	future = datetime.timedelta(hours=12)
        past = datetime.timedelta(hours=-12)
        begin_time = unicode(datetime.datetime.now() + past)
        end_time = unicode(datetime.datetime.now() + future)
        begin_time = begin_time[:20]
        end_time = end_time[:20]
        begin_time = begin_time.replace(' ','T')
        end_time = end_time.replace(' ','T')
        begin_time = begin_time.replace('.','+02:00')
        end_time = end_time.replace('.','+02:00')


def refresh_user(row_number):
	global begin_time
	global end_time
	time_update()
	if debug:
		print begin_time
		print end_time

	dbCon = MySQLdb.connect(host="localhost", 	
				user="ewa_datalogger", 
				passwd="ewaprojekt2017", 
				db="userhandling")
	cursor = dbCon.cursor()
	sqlQuery = "SELECT * FROM  tbl_userlogin"	
	cursor.execute(sqlQuery)
	rows = cursor.fetchall()
	numrows = int (cursor.rowcount)
	user = rows[row_number]
	username = user[1]
	power_number = user[3]
	water_number = user[4]
	print power_number
	print water_number
			
	if not power_number and not water_number: #water_number = False, power_number = False
		return username, numrows, False, False	#row_number, water, power 

	if not water_number and power_number: #water_number = False, power_number = True
	################### Strom ###############
		replacement_power = 'Project_EWA_' + unicode(datetime.datetime.now())
		tree = ET.parse("/var/www/data/Arlberghaus_Strom.xml")
		root = tree.getroot()
		
		for power in root.iter('{amis:com.siemens.ptd.amis}device'):
			power.text = power_number
	
		for activation_time in root.iter('{amis:com.siemens.ptd.amis}activationTime'):
			activation_time.text = begin_time 
	
		for delivery_time in root.iter('{amis:com.siemens.ptd.amis}deliveryTime'):	
			delivery_time.text = end_time

		for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
        		begin_time.text = replacement_power
	
		tree = ET.ElementTree(root)
		with open("/var/www/data/Arlberghaus_Strom.xml", "w") as f:
	        	tree.write(f)
			f.close()


	################## Strom Poll ###########
        	tree = ET.parse("/var/www/data/Arlberghaus_Strom_poll.xml")
        	root = tree.getroot()

        	for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
                	begin_time.text = replacement_power

        	tree = ET.ElementTree(root)
       	 	with open("/var/www/data/Arlberghaus_Strom_poll.xml", "w") as g:
                	tree.write(g)
		
		return username, numrows, False, True, replacement_power 	

	if not power_number and water_number:
	################## Wasser ###############
		replacement_water = 'Project_EWA_' + unicode(datetime.datetime.now())
        	tree = ET.parse("/var/www/data/Arlberghaus_Wasser.xml")
        	root = tree.getroot()
		
		for water in root.iter('{amis:com.siemens.ptd.amis}device'):
			water.text = water_number
		
		for activation_time in root.iter('{amis:com.siemens.ptd.amis}activationTime'):
			time_update()
			activation_time.text = begin_time
	
		for delivery_time in root.iter('{amis:com.siemens.ptd.amis}deliveryTime'):
			delivery_time.text = end_time	

        	for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
                	begin_time.text = replacement_water
        
		tree = ET.ElementTree(root)
        	with open("/var/www/data/Arlberghaus_Wasser.xml", "w") as h:
                	tree.write(h)
			h.close()


	################## Wasser Poll ###########
        	tree = ET.parse("/var/www/data/Arlberghaus_Wasser_poll.xml")
        	root = tree.getroot()

        	for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
                	begin_time.text = replacement_water

        	tree = ET.ElementTree(root)
        	with open("/var/www/data/Arlberghaus_Wasser_poll.xml", "w") as i:
                	tree.write(i)
		return username, numrows, True, False, replacement_water


	if water_number and power_number:
	################### Strom ###############
		replacement_power = 'Project_EWA_' + unicode(datetime.datetime.now())
		tree = ET.parse("/var/www/data/Arlberghaus_Strom.xml")
		root = tree.getroot()

		for power in root.iter('{amis:com.siemens.ptd.amis}device'):
			power.text = power_number
	
		for activation_time in root.iter('{amis:com.siemens.ptd.amis}activationTime'):
			activation_time.text = begin_time 
	
		for delivery_time in root.iter('{amis:com.siemens.ptd.amis}deliveryTime'):	
			delivery_time.text = end_time

		for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
        		begin_time.text = replacement_power
	
		tree = ET.ElementTree(root)
		with open("/var/www/data/Arlberghaus_Strom.xml", "w") as f:
	        	tree.write(f)
			f.close()


	################## Strom Poll ###########
        	tree = ET.parse("/var/www/data/Arlberghaus_Strom_poll.xml")
        	root = tree.getroot()

        	for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
                	begin_time.text = replacement_power

        	tree = ET.ElementTree(root)
        	with open("/var/www/data/Arlberghaus_Strom_poll.xml", "w") as g:
                	tree.write(g)


	################## Wasser ###############
		replacement_water = 'Project_EWA_' + unicode(datetime.datetime.now())
        	tree = ET.parse("/var/www/data/Arlberghaus_Wasser.xml")
        	root = tree.getroot()
		
		for water in root.iter('{amis:com.siemens.ptd.amis}device'):
			water.text = water_number

		for activation_time in root.iter('{amis:com.siemens.ptd.amis}activationTime'):
			time_update()
			activation_time.text = begin_time
	
		for delivery_time in root.iter('{amis:com.siemens.ptd.amis}deliveryTime'):
			delivery_time.text = end_time	

        	for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
                	begin_time.text = replacement_water
        
		tree = ET.ElementTree(root)
        	with open("/var/www/data/Arlberghaus_Wasser.xml", "w") as h:
                	tree.write(h)
			h.close()


	################## Wasser Poll ###########
        	tree = ET.parse("/var/www/data/Arlberghaus_Wasser_poll.xml")
        	root = tree.getroot()

        	for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
                	begin_time.text = replacement_water

        	tree = ET.ElementTree(root)
        	with open("/var/www/data/Arlberghaus_Wasser_poll.xml", "w") as i:
                	tree.write(i)	

		return username, numrows, True, True, replacement_water, replacement_power


def refresh_id(row_number, replacement, index):
	dbCon = MySQLdb.connect(host="localhost", 	
				user="ewa_datalogger", 
				passwd="ewaprojekt2017", 
				db="userhandling")
	cursor = dbCon.cursor()
	sqlQuery = "SELECT * FROM  tbl_userlogin"	
	cursor.execute(sqlQuery)
	rows = cursor.fetchall()
	numrows = int (cursor.rowcount)
	user = rows[row_number]
	username = user[1]
	power_number = user[3]
	water_number = user[4]
	print power_number
	print water_number
	if not power_number and not water_number: #water_number = False, power_number = False
		return username, numrows, False, False	#row_number, water, power 

	if not water_number and power_number: #water_number = False, power_number = True
	################## Strom Poll ###########
        	tree = ET.parse("/var/www/data/Arlberghaus_Strom_poll.xml")
        	root = tree.getroot()

		for power in root.iter('{amis:com.siemens.ptd.amis}device'):
                	power.text = power_number

        	for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
                	begin_time.text = replacement[index]

        	tree = ET.ElementTree(root)
       	 	with open("/var/www/data/Arlberghaus_Strom_poll.xml", "w") as g:
                	tree.write(g)
		
		return username, numrows, False, True, replacement[index]

	if not power_number and water_number:
	################## Wasser Poll ###########
        	tree = ET.parse("/var/www/data/Arlberghaus_Wasser_poll.xml")
        	root = tree.getroot()

		for water in root.iter('{amis:com.siemens.ptd.amis}device'):
                	water.text = water_number


        	for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
                	begin_time.text = replacement[index]

        	tree = ET.ElementTree(root)
        	with open("/var/www/data/Arlberghaus_Wasser_poll.xml", "w") as i:
                	tree.write(i)
		return username, numrows, True, False, replacement[index]


	if water_number and power_number:
	################## Strom Poll ###########
        	tree = ET.parse("/var/www/data/Arlberghaus_Strom_poll.xml")
        	root = tree.getroot()

		for power in root.iter('{amis:com.siemens.ptd.amis}device'):
                        power.text = power_number

        	for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
                	begin_time.text = replacement[index]

        	tree = ET.ElementTree(root)
        	with open("/var/www/data/Arlberghaus_Strom_poll.xml", "w") as g:
                	tree.write(g)

	################## Wasser Poll ###########
        	tree = ET.parse("/var/www/data/Arlberghaus_Wasser_poll.xml")
        	root = tree.getroot()

		for water in root.iter('{amis:com.siemens.ptd.amis}device'):
                        water.text = water_number

        	for begin_time in root.iter('{amis:com.siemens.ptd.amis}request'):
			index_1 = index + 1
                	begin_time.text = replacement[index_1]

        	tree = ET.ElementTree(root)
        	with open("/var/www/data/Arlberghaus_Wasser_poll.xml", "w") as i:
                	tree.write(i)	

		return username, numrows, True, True, replacement[index], replacement[index_1]
