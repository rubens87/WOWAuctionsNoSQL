"""
SALEM auctions! 
Simple and Lazy Exporter/Importer of MongoDB
At last it will be, when it's done!

Blizzard's methodology of termins :)

Feel free to take it, modify, expand, explore!

What it does?
It takes json file  representing server auctions and puts it into mongoDB
Its part of NoSQL course homework for dr W.Bzyl (that tutorials guy from wykop - polish reddit/digg)
Created by the Internet, borrowed and coded by Lukasz Kedron (rubens87@github)
"""

import pymongo
import json
from pymongo import Connection

"""
here is going to be config the whole thing:
"""

#dbsetup

port = 27017 #now
host = 'localhost'

#dbchooser
dbname = "burning_legion"

#filechooser
json_sourceFile = "auctionsBL.json"




#Connecting to db
connection = Connection('localhost', 27017)
f=open("auctionsBL.json", "r")
post = json.loads(f.read())
db = connection['wow-auctions']
posts = db.auctions

#adding alliance
for element in post['alliance']['auctions']:
	posts.insert(element)

#adding horde
db = connection['horde']
for element in post['horde']['auctions']:
	post.insert(element)

#adding neutral
db = connection['neutral']
for element in post['netural']['auctions']:
	post.insert(element)
"""
posts = db.posts
for post in post.find():
	
"""	
