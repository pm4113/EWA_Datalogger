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


debug = True
url = "http://194.208.52.114:8080/axis2/services/DataCollection?wsdl"
headers = {'Content-type':'text/html'}
replacement = 'Project_EWA_' + unicode(datetime.datetime.now())
get_response = True
end_of_user = True
end_of_user_response = False
response_strom = 0
response_wasser = 0
error_handling_timeout = 0
row_count = 0
request_handler = []
index_count = 0
then = datetime.datetime.now() + timedelta(minutes = 3000)

while(True):
	now = datetime.datetime.now()
	end_of_user = True
	row_count = 0
	request_handler = []
	if now > then:
		then = datetime.datetime.now() + timedelta(minutes = 3000)
		while (end_of_user):
			print row_count
			feedback = refresh_user(row_count)
			if debug:
				print "Du befindest dich in der end of user schleife!!"
				for i in feedback:
					print i
			row_count += 1
			if row_count <= feedback[1]:
				Kunde_request = open_Kunde()
				if row_count == feedback[1]:	
					end_of_user = False	
					row_count = 0
					index_count = 0

				if (feedback[2] and feedback[3]):           
					Kunde_strom = requests.post(url, data=Kunde_request[0], headers=headers) #Strom
					Kunde_wasser = requests.post(url, data=Kunde_request[1], headers=headers) #Wasser
					request_handler.append(feedback[5])
					request_handler.append(feedback[4])
					end_of_user_response = True
					if debub:
						print "Alle Daten vorhanden!"				
						print "--------- Request gesendet ---------"
						print Kunde_request[0]
						print Kunde_request[1]
						print "------------------------------------"
						print request_handler
						print Kunde_strom.content
						print Kunde_wasser.content
						print "---------------Ende-----------------"	

				elif not feedback[2] and feedback[3]:
					Kunde_strom = requests.post(url, data=Kunde_request[0], headers=headers) #Strom
					request_handler.append(feedback[4])
					end_of_user_response = True
					if debug:
						print "Keine Wasserdaten vorhanden!"				
						print "--------- Request gesendet ---------"
						print Kunde_request[0]
						print "------------------------------------"
						print request_handler
						print Kunde_strom.content	
						print "--------------Ende------------------"	
			
				elif not feedback[3] and feedback[2]:
					Kunde_wasser = requests.post(url, data=Kunde_request[1], headers=headers) #Wasser
					request_handler.append(feedback[4])
					end_of_user_response = True
					if debug:
						print "Keine Stromdaten vorhanden!"					
						print "--------- Request gesendet ---------"
						print Kunde_request[1]
						print "------------------------------------"
						print request_handler	
						print Kunde_wasser.content
						print "----------Ende--------------------- "	
				
				elif not feedback[2] and not feedback[3]:
					end_of_user_response = True
					if debug:
						print "Keine Daten vorhanden!"
					
			else:
				end_of_user = False



		while (end_of_user_response):
				print row_count
				feedback = refresh_id(row_count, request_handler, index_count)
				if debug:
					print "Du befindest dich in der end_of_user_response schleife!!!"
					for i in feedback:
						print i
				row_count += 1
				if row_count <= feedback[1]:
					Kunde_request = open_Kunde()
					if row_count == feedback[1]:	
						end_of_user_response = False
						row_count = 0
						index_count = 0

					if (feedback[2] and feedback[3]):           	
						index_count += 2
						insert_into_db = True
						if debub:
							print "Alle Daten vorhanden!"				

					elif not feedback[2] and feedback[3]:	
						index_count += 1
						insert_into_db = True
						if debug:
							print "Keine Wasserdaten vorhanden!"				
			
					elif not feedback[3] and feedback[2]: 
						index_count += 1
						insert_into_db = True	
						if debug:
							print "Keine Stromdaten vorhanden!"				
				
					elif not feedback[2] and not feedback[3]:
						insert_into_db = False
						if debug:
							print "Keine Daten vorhanden!"

				else:
					end_of_user_response = False			
					row_count = 0
					index_count = 0


				while(insert_into_db):
					error_handling_timeout += 1                
					time.sleep(10)
		
					if (feedback[2] and feedback[3]):           	
  		   				Kunde_strom_poll = requests.post(url, data=Kunde_request[2], headers=headers)
     						Kunde_wasser_poll = requests.post(url, data=Kunde_request[3], headers=headers)
#						index_count += 2
						insert_into_db = True
						if debub:
							print "Alle Daten vorhanden!"				
							print "--------- Response empfangen ---------"
							print "----------------Strom-----------------"
    							print Kunde_strom_poll.content 
							print "---------------Wasser-----------------"
							print Kunde_wasser_poll.content
							print "--------------------------------------"

					elif not feedback[2] and feedback[3]:
     						Kunde_strom_poll = requests.post(url, data=Kunde_request[2], headers=headers)	
#						index_count += 1
						insert_into_db = True
						if debug:
							print "Keine Wasserdaten vorhanden!"				
							print "--------- Response empfangen ---------"
    							print Kunde_strom_poll.content 	
							print "--------------------------------------"
			
					elif not feedback[3] and feedback[2]:
     						Kunde_wasser_poll = requests.post(url, data=Kunde_request[3], headers=headers) 
#						index_count += 1
						insert_into_db = True	
						if debug:
							print "Keine Stromdaten vorhanden!"				
							print "--------- Response empfangen ---------"
							print Kunde_wasser_poll.content
							print "--------------------------------------"
				
					elif not (feedback[2] and feedback[3]):
						if debug:
							print "Keine Daten vorhanden!"

					with open("/var/www/data/Arlberghaus_Response_Strom.xml", "wb") as d:
						d.write(Kunde_strom_poll.text)
						d.close()
						Kunde_response_strom = get_data_kunde_strom()
						print "Aktueller Stromstand: " + str(Kunde_response_strom)

					with open("/var/www/data/Arlberghaus_Response_Wasser.xml", "wb") as f:
						f.write(Kunde_wasser_poll.text)
						f.close()
						Kunde_response_wasser = get_data_kunde_wasser()
						print "Aktueller Wasserstand: " + str(Kunde_response_wasser)
		
					if  Kunde_response_wasser > 0:
						response_wasser = Kunde_response_wasser
					if Kunde_response_strom > 0:
						response_strom = Kunde_response_strom
					if feedback[2] and feedback[3]:
						if (response_strom > 0 and response_wasser > 0) or error_handling_timeout == 10:	
							writeIntoDB(feedback, response_strom, response_wasser)
							if debug:
								print "--------------------------"
								print "Response_Wasser:"
								print response_wasser
								print "Response_Strom:"
								print response_strom
								print "---------------------------"
							response_wasser = 0
							response_strom = 0	
							error_handling_timeout = 0
							insert_into_db = False
		
					elif not feedback[2] and feedback[3]:
						if response_strom > 0 or error_handling_timeout == 10:	
							writeIntoDB(feedback, response_strom, response_wasser)
							if debug:
								print "--------------------------"
								print "Response_Strom:"
								print response_strom	
								print "---------------------------"
							response_wasser = 0
							response_strom = 0	
							error_handling_timeout = 0
							insert_into_db = False

					elif not feedback[3] and feedback[2]:
						if response_wasser > 0 or error_handling_timeout == 10:	
							writeIntoDB(feedback, response_strom, response_wasser)
							if debug:
								print "--------------------------"
								print "Response_Wasser:"
								print response_wasser	
								print "---------------------------"
							response_wasser = 0
							response_strom = 0	
							error_handling_timeout = 0
							insert_into_db = False
