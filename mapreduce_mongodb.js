// prosty map reduce dla mongoDB, pokazujacy, kto ile zarobi, w przypadku gdy wszystkie jego rzeczy się sprzedadza

var map = function() {
	emit(this.onwer, {rich: this.buyout});
};

var reduce = function(key, values) {
	var sum = 0;
	values.forEach(function(doc){
		sum+= doc.rich;
	});
	return {incoming_cash: sum}
};

var op = db.auctions.mapReduce(map, reduce, {out: "Richest_people"});

// get result from shell

db[op.result].find();
