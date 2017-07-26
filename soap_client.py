import requests
import time
import datetime
import xml.etree.ElementTree as ET
from refresh_files import *
from open_files import *
from identify_data import *
from write_database import *


debug = False
url = "http://194.208.52.114:8080/axis2/services/DataCollection?wsdl"
headers = {'Content-type':'text/html'}
replacement = 'Project_EWA_' + unicode(datetime.datetime.now())
get_response = True

refresh_Arlberghaus()
Kunde1_request = open_Arlberghaus()
if debug:
	print Kunde1_request[0]
	print Kunde1_request[1]
	print Kunde1_request[2]
	print Kunde1_request[3]
                                   
while(True):
#	get_response = True
#	Kunde1_strom = requests.post(url, data=Kunde1_request[0], headers=headers) #Strom
#	Kunde1_wasser = requests.post(url, data=Kunde1_request[1], headers=headers) #Wasser
#	if debug:
#		print Kunde1_strom.content
#		print Kunde1_wasser.content
#	while(get_response):                   
			time.sleep(10)
 #    		Kunde1_strom_poll = requests.post(url, data=Kunde1_request[2], headers=headers)
  #   		Kunde1_wasser_poll = requests.post(url, data=Kunde1_request[3], headers=headers)
#		if debug:
 #   			print Kunde1_strom_poll.content 
#			print Kunde1_wasser_poll.content
		
#		with open("Arlberghaus_Response_Strom.xml", "wb") as d:
#			d.write(Kunde1_strom_poll.text)
#			d.close()
			Kunde1_response_strom = get_data_kunde1_strom()
			print "Aktueller Stromstand: " + str(Kunde1_response_strom)

#		with open("Arlberghaus_Response_Wasser.xml", "wb") as f:
#			f.write(Kunde1_wasser_poll.text)
#			f.close()
			Kunde1_response_wasser = get_data_kunde1_wasser()
			print "Aktueller Wasserstand: " + str(Kunde1_response_wasser)
		
			if  Kunde1_response_wasser > 0:
				if Kunde1_response_strom > 0:
					get_response = False
					writeIntoDB(Kunde1_response_strom, Kunde1_response_wasser)
		


