import requests
import time
import datetime
import xml.etree.ElementTree as ET

url = "http://194.208.52.114:8080/axis2/services/DataCollection?wsdl"
headers = {'Content-type':'text/html'}

search = 'Project_EWA'
replacement = 'Project_EWA_' + unicode(datetime.datetime.now())
print replacement
with open("Arlberghaus_Strom.xml") as f:
        Kunde1_Strom = f.read()
      
with open("Arlberghaus_Strom_poll.xml") as g:
        Kunde1_Strom_poll = g.read()

with open("Arlberghaus_Wasser.xml") as h:
        Kunde1_Wasser = h.read()
       
with open("Arlberghaus_Wasser_poll.xml") as i:
        Kunde1_Wasser_poll = i.read()

#itree = ET.parse("Arlberghaus_Strom.xml")
#root = tree.getroot()

#for begin_time in root.iter("amis:request"):
#	begin_time.text = replacement
#tree = ET.ElementTree(root)
#with open("Arlberghaus.xml", "w") as f:
#	tree.write(f)

ARL_Strom = requests.post(url, data=Kunde1_Strom, headers=headers)
ARL_Wasser = requests.post(url, data=Kunde1_Wasser, headers=headers)
print ARL_Strom.content            
print ARL_Wasser.content           
                                   
while(True):                        
        time.sleep(10)
        ARL_Strom_poll = requests.post(url, data=Kunde1_Strom_poll, headers=headers)
        ARL_Wasser_poll = requests.post(url, data=Kunde1_Wasser_poll, headers=headers)
        print ARL_Strom_poll.content 
	print ARL_Wasser_poll.content
