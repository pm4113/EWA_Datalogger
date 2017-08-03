from pdb import set_trace as bp
import MySQLdb
import time

def writeIntoDB(database_info, strom, wasser):
	if database_info[2] and database_info[3]:
		if (wasser != 0 and strom != 0):	
			try:
				table = database_info[0]
				dbCon = MySQLdb.connect(host="localhost", 	
							user="ewa_datalogger", 
							passwd="ewaprojekt2017", 
							db="datastorage")
				cursor = dbCon.cursor()

				timestamp = int(time.time()) * 1000
				record = (timestamp , wasser, strom)
				sqlQuery = " INSERT INTO " + table + " VALUES(DEFAULT, %s , %s, %s) "
				cursor.execute(sqlQuery, record) #execute query
				print "You are in database"
				print "Strom: " + str(strom)
				print "Wasser: " + str(wasser)
				dbCon.commit()	#commit transaction

			except:
				print "Keine Verbindung zu Datenbank"


	elif not database_info[2] and database_info[3]:
		if (strom != 0):	
			try:
				wasser = None
				table = database_info[0]
				dbCon = MySQLdb.connect(host="localhost", 	
							user="ewa_datalogger", 
							passwd="ewaprojekt2017", 
							db="datastorage")
				cursor = dbCon.cursor()

				timestamp = int(time.time()) * 1000
				record = (timestamp , wasser, strom)
				sqlQuery = " INSERT INTO " + table + " VALUES(DEFAULT, %s , %s, %s) "
				cursor.execute(sqlQuery, record) #execute query
				print "You are in database"
				print "Strom: " + str(strom)
				dbCon.commit()	#commit transaction

			except:
				print "Keine Verbindung zu Datenbank"


	elif not database_info[3] and database_info[2]:
		if (wasser != 0):	
			try:
				strom = None
				table = database_info[0]
				dbCon = MySQLdb.connect(host="localhost", 	
							user="ewa_datalogger", 
							passwd="ewaprojekt2017", 
							db="datastorage")
				cursor = dbCon.cursor()

				timestamp = int(time.time()) * 1000
				record = (timestamp , wasser, strom)
				sqlQuery = " INSERT INTO " + table + " VALUES(DEFAULT, %s , %s, %s) "
				cursor.execute(sqlQuery, record) #execute query
				print "You are in database"
				print "Strom: " + str(strom)
				print "Wasser: " + str(wasser)
				dbCon.commit()	#commit transaction

			except:
				print "Keine Verbindung zu Datenbank"
