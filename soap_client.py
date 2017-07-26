#!/usr/bin/env python

from pdb import set_trace as bp
import requests
import time
from datetime import datetime, timedelta
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
response_strom = 0
response_wasser = 0
error_handling_timeout = 0
then = datetime.datetime.now() + timedelta(minutes = 60)

while(True):
	now = datetime.datetime.now()
#	time.sleep(2800)
	if now > then:
		then = datetime.datetime.now() + timedelta(minutes = 60)
		refresh_Arlberghaus()
		Kunde1_request = open_Arlberghaus()
#		if debug:
#			print Kunde1_request[0]
#			print Kunde1_request[1]
#			print Kunde1_request[2]
#			print Kunde1_request[3]
                                   
		get_response = True
		Kunde1_strom = requests.post(url, data=Kunde1_request[0], headers=headers) #Strom
		Kunde1_wasser = requests.post(url, data=Kunde1_request[1], headers=headers) #Wasser
		if debug:
			print "--------- Request gesendet ---------"
			print Kunde1_strom.content
			print Kunde1_wasser.content
			print " "
		while(get_response):
			error_handling_timeout += 1                
			time.sleep(10)
     			Kunde1_strom_poll = requests.post(url, data=Kunde1_request[2], headers=headers)
     			Kunde1_wasser_poll = requests.post(url, data=Kunde1_request[3], headers=headers)
			if debug:
				print "--------- Response empfangen ---------"
    				print Kunde1_strom_poll.content 
				print Kunde1_wasser_poll.content
				print " "
		
			with open("/var/www/data/Arlberghaus_Response_Strom.xml", "wb") as d:
				d.write(Kunde1_strom_poll.text)
				d.close()
				Kunde1_response_strom = get_data_kunde1_strom()
				print "Aktueller Stromstand: " + str(Kunde1_response_strom)

			with open("/var/www/data/Arlberghaus_Response_Wasser.xml", "wb") as f:
				f.write(Kunde1_wasser_poll.text)
				f.close()
				Kunde1_response_wasser = get_data_kunde1_wasser()
				print "Aktueller Wasserstand: " + str(Kunde1_response_wasser)
		
			if  Kunde1_response_wasser > 0:
				response_wasser = Kunde1_response_wasser
			if Kunde1_response_strom > 0:
				response_strom = Kunde1_response_strom
			if (response_strom > 0 and response_wasser > 0) or error_handling_timeout == 10:
				get_response = False	
				writeIntoDB(response_strom, response_wasser)
				response_wasser = 0
				response_strom = 0
				


