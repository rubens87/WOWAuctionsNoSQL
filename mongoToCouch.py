"""
This simple small script exports data from MongoDB to CouchDB, one_collection => one_db
Feel free to use it in your project. I only ask, to inform me at wheresmyjaw(at)gmail.com :)
"""


import pymongo
from pymongo import Connection
import couchdb
from couchdb import ResourceNotFound
import sys
from optparse import OptionParser

#setting up -arguments function!

parser = OptionParser()
parser.add_option("-a", "--mongohost", dest="mongohost", help="set up host of mongodb, default = localhost", default="localhost", metavar="MHOST")
parser.add_option("-b", "--mongoport", dest="mongoport", help="set port of mongodb - default = 27017", default=27017, metavar="MPORT")
parser.add_option("-c", "--mongodb", dest="mongodb", help="set up mongodb name for export, default = burning_legion", default="burning_legion", metavar="MDBNAME")
parser.add_option("-k", "--mdbcol", dest="mdbcol", help="set up mongodb collection name for export, default = auctions", default="auctions", metavar="MDBNAME")
parser.add_option("-d", "--couchhost", dest="couchhost", help="set up target couchdb host", default="localhost", metavar="CDBHOST")
parser.add_option("-e", "--couchport", dest="couchport", help="set up target couchdb port", default='5984', metavar="CDPORT")
parser.add_option("-f", "--couchdb", dest="couchdb", help="set up target couchdb name, default = wowauct", default="wowauct", metavar="CDBASE")
(options, args) = parser.parse_args()

# Connecting to Couchdb
couchServer = couchdb.Server('http://'+options.couchhost+':'+options.couchport)
print options.couchdb
try:
	dbC = couchServer[options.couchdb]
except:
	dbC = couchServer.create(options.couchdb)

# Connecting to Mongodb

dbconnect = Connection(options.mongohost, int(options.mongoport))
db = dbconnect[options.mongodb]
kolekcja = db[options.mdbcol]

#seting up progress bar
nofdb = kolekcja.find().count()

#eksportuj
if nofdb == 0:
	print "Zla baza zadnych wybrana"
else:
	i = 0
	for cursor in kolekcja.find():
		del cursor["_id"]
		dbC.save(cursor)
		sys.stdout.write("przerzucono: %d z %d \r" %(i, nofdb))
		i = i + 1


#i love python it's so clean and short!

