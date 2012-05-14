function(doc) {
	emit(doc.item, (doc.buyout/(doc.quantity*10000)));
}

function(keys, values, rereduce) {
	var srednia = sum(values)/values.length;
	var temp = 0;
	for(var i = 0; i < values.length; i++){
		temp = values[i] - srednia;
		temp = temp*temp;
		sigma += temp;
	}
	//sigma = Math.sqrt(sigma);
	//return {Srednia_Cena: srednia, odchStd: sigma}
	return srednia;
}
