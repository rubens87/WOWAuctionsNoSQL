#-*- coding: utf-8 -*-

from pymongo import Connection
from bson.code import Code
from optparse import OptionParser

"""
here is going to be config the whole thing:
"""

parser = OptionParser()
parser.add_option("-n", "--name", dest="dbname", help="give name of database to create", default="burning_legion", metavar="DBNAME")
parser.add_option("-m", "--host", dest="dbhost", help="give host name of database", default="localhost", metavar="DBHOST")
parser.add_option("-p", "--port", dest="dbport", help="give port", default=27017, metavar="DBPORT")
(options, args) = parser.parse_args()

connection = Connection(options.dbhost, int(options.dbport))
db = connection[options.dbname]

map = Code("""function() {
	emit(this.owner, this.buyout);
};""")
		   
reduce = Code("""function(key, values) {
	var sum = 0;
	for(var i = 0; i < values.length; i++){
		sum += values[i];
	}
	return sum;
};""")
		  

result = db.auctions.map_reduce(map, reduce, "full_response=True")
for x in result.find().sort(u'value',-1).limit(10):
	print x

