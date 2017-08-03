import xml.etree.ElementTree as ET

debub = True
strom_data = ['0','0','0','0','0','0','0','0','0','0']
wasser_data = ['0','0','0','0','0','0','0','0','0','0']
def get_data_kunde_strom():
	strom_data = ['0','0','0','0','0','0','0','0','0','0']
	i = 0 
	tree = ET.parse("/var/www/data/Arlberghaus_Response_Strom.xml")
	root = tree.getroot()

	for get_data in root.iter('{amis:com.siemens.ptd.amis}integer'):
		strom_data.insert(i, get_data.text)
		i = i+1	
	return_value = [strom_data[index] for index in [1]]
	return_value = map(int, return_value)
	return_value = return_value[0]
#	print return_value
	if strom_data == 0:
		return_value = 0
	return return_value

def get_data_kunde_wasser():	
	wasser_data = ['0','0','0','0','0','0','0','0','0','0']
	i = 0
	tree = ET.parse("/var/www/data/Arlberghaus_Response_Wasser.xml")
	root = tree.getroot()
	
	for get_data in root.iter('{amis:com.siemens.ptd.amis}integer'):
		wasser_data.insert(i, get_data.text)
		i = i+1	
	return_value = [wasser_data[index] for index in [3]]
	return_value = map(int, return_value)
	return_value = return_value[0]
#	print return_value
	if wasser_data == 0:
		return_value = 0
	return return_value
