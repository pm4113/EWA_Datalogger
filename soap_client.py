import requests
import time
import datetime
import xml.etree.ElementTree as ET
from refresh_files import *
from open_files import *

debug = True
url = "http://194.208.52.114:8080/axis2/services/DataCollection?wsdl"
headers = {'Content-type':'text/html'}
replacement = 'Project_EWA_' + unicode(datetime.datetime.now())
get_data = True

refresh_Arlberghaus()
Kunde1 = open_Arlberghaus()
if debug:
	print Kunde1[0]
	print Kunde1[1]
	print Kunde1[2]
	print Kunde1[3]
                                   
while(True):
	ARL_Strom = requests.post(url, data=Kunde1[0], headers=headers)
	ARL_Wasser = requests.post(url, data=Kunde1[1], headers=headers)
	if debug:
		print ARL_Strom.content
		print ARL_Wasser.content
	while(get_data):                   
	       	time.sleep(10)
      		ARL_Strom_poll = requests.post(url, data=Kunde1[2], headers=headers)
     		ARL_Wasser_poll = requests.post(url, data=Kunde1[3], headers=headers)
		if debug:
    			print ARL_Strom_poll.content 
			print ARL_Wasser_poll.content
		
		with open("Arlberghaus_Response_Strom.xml", "wb") as d:
			d.write(ARL_Strom_poll.text)
			d.close()
		with open("Arlberghaus_Response_Wasser.xml", "wb") as f:
			f.write(ARL_Wasser_poll.text)
			f.close()
