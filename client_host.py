from pdb import set_trace as bp
import paho.mqtt.client as mqtt
from uuid import getnode
import base64
import threading
import time
import random
import threading
import sqlite3
from subprocess import Popen, PIPE


# enable or disable debug
debug = True		

#bp()
# read out the mac address to identify the machine
mac = getnode()
h = iter(hex(mac)[2:].replace('L','').zfill(12))
mac_address = ":".join(i+next(h) for i in h)
macstr = mac_address.replace(':', '').decode('hex')
machine_identifier = base64.b64encode(macstr)

#variable decleration
DBFILE = 'datalog.db'
DBNAME = 'data'
message_id = 0
data = 0
rec_client = 0
error_id = 0xFF
error_data = 0


if debug:
    print("mac address:")
    print(mac_address)
    print(machine_identifier)


error = ([0xFF])
init  = ([0x10])
datalogger = ([0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x70])

low_level_id	=   "EWA/measurement/"
low_level    	=   "EWA/measurement/"
top_level       =   str(machine_identifier)

# broker mosquitto
broker                      =  "localhost"

# subscriber topics
topic_sub_data	   	    =  low_level    + top_level + "/command/logger/data" 
topic_sub_ack		    =  low_level    + top_level + "/command/logger/acknowledge"
topic_sub_error		    =  low_level    + top_level + "/command/logger/error"
# publisher topics
topic_pub_request	    =  low_level    + top_level + "/command/host/request"
topic_pub_ack               =  low_level    + top_level + "/command/host/acknowledge" 
topic_pub_error             =  low_level    + top_level + "/command/host/error"
topic_pub_id 		    =  low_level_id + top_level + "/status"


# split message to send to pboker
def array_to_str(message_id, payload):
    payload = str(payload)
    payload = payload.replace("[","")
    payload = payload.replace("]",";")
    payload = payload.replace(" ","")
    return payload;


# split message from broker to single terms
def str_to_list(client_data): 
    client_data = client_data.replace(";",":")
    data = client_data.split(":")
    for i in data:
        print(i)

    identifier = int(data[1])
    if identifier == 0x01:      #Status
        rec_data = list([identifier])
     
    return rec_data


# read out the ID and send message from uart to broker
def publish_to_broker(message_ID, payload):
#    payload = bytearray(payload)
    if message_ID == 0x01:
	client.publish(topic_pub_data)
       

def on_connect(client, userdata, flags, rc):
    if debug:
        print("Connect with result code: " + str(rc))
    client.subscribe([  (topic_sub_data, 2), 
                        (topic_sub_ack, 2), 
                        (topic_sub_error, 2)])


def on_message(client, userdata, msg):
    global message
    if debug:
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    message = msg.payload

    if msg.topic == topic_sub_data:
	print "Data from logger: " + message
	writeIntoDB(message)

    elif msg.topic == topic_sub_ack:
	print("Acknowledge from host")

    elif msg.topic == topic_sub_error:
	print("Error from host")

    else: 
        message = error
	print("Undefined Error")


def on_publish(client, userdata, mid):
    if debug:
        print("mid: " + str(mid))


def on_subscribe(client, userdata, mid, granted_qos):
    if debug:
        print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(client, userdata, level, string):
    if debug:
        print(string)

def writeIntoDB(message):
	try:
		dbCon = sqlite3.connect(DBFILE)
		cursor = dbCon.cursor()
		timestamp = int(time.time()) * 1000
 		water = 1	# aus message herausfiltern
		current = 2	# aus message herausfiltern 
		record = (timestamp , water, current)
		sqlQuery = "insert into " + DBNAME + " (date , waterflow, current) values(? , ?, ?)"
		cursor.execute(sqlQuery , record)	#execute query
 
		dbCon.commit()	#commit transaction
		dbCon.close()
 
	except sqlite3.Error , e:
		print "SQLite error occured: " , e



class get_data(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
	
	def run(self):
		while True:
			client.publish(topic_pub_request)
			time.sleep(5)


get_data_thread = get_data()
get_data_thread.start()


client = mqtt.Client()
# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.publish(topic_pub_id, "Online", qos = 2, retain = True)
client.will_set(topic_pub_id, "Offline", qos = 2, retain = True)

# Connect
client.connect(host = broker, port = 1883, keepalive = 60)
client.loop_forever()

