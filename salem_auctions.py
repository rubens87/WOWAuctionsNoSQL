"""
SALEM auctions! 
Simple and Lazy Exporter/Importer of MongoDB
At last it will be, when it's done!

Blizzard's methodology of termins :)

Feel free to take it, modify, expand, explore!

What it does?
It takes json file  representing server auctions and puts it into mongoDB

What has to be changed?Many things!
First of all we want to make it more flexible (-args) *updated DONE
Secondly maybe we change a bit that json to represent data in diffrend way.


It is part of NoSQL course homework for dr W.Bzyl (that tutorials guy from wykop - polish reddit/digg)

Created by the Internet, 
borrowed and coded by Lukasz Kedron (rubens87@github)
"""

import pymongo
import json
from pymongo import Connection
from optparse import OptionParser

"""
here is going to be config the whole thing:
"""

parser = OptionParser()
parser.add_option("-f", "--file", dest="jsonname", help="give json filename, as a argument", default="auctionsBL.json", metavar="FILE")
parser.add_option("-n", "--name", dest="dbname", help="give name of database to create", default="burning_legion", metavar="DBNAME")
parser.add_option("-m", "--host", dest="dbhost", help="give host name of database", default="localhost", metavar="DBHOST")
parser.add_option("-p", "--port", dest="dbport", help="give port", default=27017, metavar="DBPORT")
(options, args) = parser.parse_args()



#dbsetup

port = options.dbport
host = options.dbhost

#dbchooser
dbname = options.dbname

#filechooser
json_sourceFile = options.jsonname




#Connecting to db
connection = Connection(host, int(options.dbport))
f=open(json_sourceFile, "r")
post = json.loads(f.read())
db = connection[dbname]
posts = db.auctions

#adding alliance
for element in post['alliance']['auctions']:
	posts.insert(element)

#adding horde
db = connection['horde']
for element in post['horde']['auctions']:
	posts.insert(element)

#adding neutral
db = connection['neutral']
for element in post['neutral']['auctions']:
	posts.insert(element)
"""
posts = db.posts
for post in post.find():
	
"""	
