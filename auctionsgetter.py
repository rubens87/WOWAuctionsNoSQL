import urllib
import json

"""
This is work in progress!
Things that do at the moment:
1. gets list of servers from blizzard's mostly RESTful API
2. saves that list to .swsl text file
3. opens that list
4. gets all auctions from blizzard's mostly RESTful API

Things that it should do in future:
1. have options and help!:
	options:
		a) get server list and save to serwery.swsl
		b) load server list (serwery.swsl) from file and get and save auctions.json file
2. Develop into downloading other stuff than auctions:
	a) items
	b) chars
	c) guilds
	
made by: Tutorials, written by: LKedron
Gdansk 2012

**** NOT COPYRIGHT STUFF ****
Take it, do with whatever you want. If you would kindly mention using it in your project would be nice,
if not i'll understand. Anyway, writing this stuff took longer than coding those script lines.

"""

host = 'http://eu.battle.net'
 
#get server list
result = json.loads(urllib.urlopen(host+'/api/wow/realm/status/').read())


#get slug from server list
servers = []
for name in result["realms"]:
	servers.append(name["slug"])

#save slug name into file .swsl OPEN Stupid WoW Server List format	
f = open("serwery.swsl", "w")
f.write(",".join(servers))
f.close()

#open .swsl file to get server list
f = open("serwery.swsl", "r")
serwery = f.read()
serwery = serwery.split(",")
f.close()


# temp = json.loads(urllib.urlopen(temp).read())

#creating localfile to save json
f = open("auctions.json", "a")

#saving exImport to localfile

def exImport(servers):
	for serwer in servers:
		#print for checking on which server we are
		print 'downloading'+server+'!!!\n'+host+'/api/wow/action/data/'+serwer
		temp = json.loads(urllib.urlopen(host+'/api/wow/auction/data/'+serwer).read())
		#tutaj tez checkstatus, taki slo-mo matrix!
		print 'the adress of auctions is: \n '+temp
		temp = urllib.urlopen(temp['files'][0]['url']).read()
		f.write(temp)
		
exImport(serwery)
f.close()




# creating one huge ~1.1GB json file O__o
f = open("auction_Srv.json", "w++")

