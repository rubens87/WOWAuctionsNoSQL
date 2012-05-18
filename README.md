Zadania na laboratoria Bazy NoSQL


Te skrypty importuja dane z serwerow gry komputerowej World of Warcraft, ktore obejmuja
dom aukcyjny. Jest to zrzut z konkretnego dnia. Dane sa zapisywane do JSON'a, nastepnie 
przerzucane do Mongodb, z Mongodb do Couchdb, na bazie mongodb jest wykonywany mapReduce.
Na potrzeby przykladu, tylko 1 serwer zostal uzyty. W przypadku importu wszystkiego - wyniesie to kilka GB danych.



Potrzebne biblioteki do odpalenia plików:

pymongo
instalacja:
    git clone git://github.com/mongodb/mongo-python-driver.git pymongo
    cd pymongo/
    python setup.py install

couchdbkit
instalacja:
    wget http://peak.telecommunity.com/dist/ez_setup.py
    sudo python ez_setup.py
    wget http://pypi.python.org/packages/2.6/C/CouchDB/CouchDB-0.8-py2.6.egg
    sudo easy_install CouchDB-0.8-py2.6.egg
    

Skrypty
*    salem_auctions.py - importuje dane z pliku jsona do bazy mongodb
*    mongoToCouch.py - exportuje baze danych z MongoDB to COuchDB
*    mongo_mapreduce.py - mapreduce wyrzucajacy 10 osob, ktore maja aukcje o najwyzszej wartosci

Uruchamianie:

salem_auctions.py
    
    python salem_auctions -f [nazwa_pliku_json] -n [nazwa_bazy_danych] -m [host] -p [port] 

w przypadku braku argumentow wykonuje sie:

    python salem_auctions -f auctionsBL.json -n burning_legion -m localhost -p 27017
    
mongoToCouch.py:

    python mongoToCouch.py -a [mongohost] -b [mongoport] -c [mongodbname] -k[mongoCollection] -d[couchHost] -e[couchPort]  -f[couchDbName]

w przypadku braku argumentów, argumenty standardowe jezeli chodzi o hosty i porty: localhost i oppowiednio 27017(mongo) i 5984(couch)
baza mongo to: burning_legion, a kolekcja: auctions. Baza w couchu założona byłąby jako wowauct.
updejt: dowiedzialem sie dopiero pod koniec, ze Couchdb nie lubie uppercasów w nazwach baz!

mongo_mapreduce.py

    python mongo_mapreduce.py -n [dbname] -m [dbhost] -p [dbport]

przy braku argumentów uruchomi sie:

    python mongo_mapreduce.py -n burning_legion -m localhost -p 27017
    


