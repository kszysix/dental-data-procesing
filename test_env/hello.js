// Create a request variable and assign a new XMLHttpRequest object to it.



function sendHello(){
	var request = new XMLHttpRequest();
	request.open('GET', 'http://127.0.0.1:5000/mic', false);

	request.send();
	var obj = JSON.parse(request.response);
	console.log(obj.result);
	document.getElementById('output1').innerHTML = obj.result;
	if(obj.next == 1){

	}
	while(obj.next == 1){
		request.open('GET', 'http://127.0.0.1:5000/mic', false);
		request.send();
		obj = JSON.parse(request.response);
		console.log(obj.result);
		document.getElementById('output1').innerHTML = obj.result;
	}
	// fetch('http://127.0.0.1:5000/first')
 //    .then(response => response.json())
 //  	.then(data => console.log(data));
}
// Send request


function createTable(){
	console.log("tableName: "+document.getElementById("tableName").value);
	// fetch('http://127.0.0.1:5000/createTable', {
	// method: 'POST',
	// body: {"tableName": document.getElementById("tableName").value}, // The data
	// headers: {
	// 	'Content-Type': 'application/json'
	// }})
	// .then(response => response.json())
	// .then(data => console.log(data));

}

function connectToDatabase(){
	fetch('http://127.0.0.1:5000/connectToDatabase', {
	method: 'GET'
	})
	.then(response => response.json())
	.then(data => console.log(data.log));
}