// Get response for distance criteria
function distance_range() {
    // Get the current distance value from the text input box
    let selected_distance = document.getElementById('distance_range').value;

    // This URL path is going to be the route defined in app.py
    let theURL= '/distance/' + selected_distance;
    console.log(theURL);

    // Fetch is a Javascript function that sends a request to a server
    fetch(theURL)
        .then(response=>response.json()) // Convert response to JSON

        .then(function(response) {
            console.log(response)

            const table_id = document.getElementById("table_id");
            const distance = document.getElementById("distance"); 
            const button = document.getElementById("button"); 
            const timestamp = document.getElementById("timestamp");

            if (response['error'] == "no_error"){
                table_id.innerHTML = "ID: " + response['id'].toString();
                distance.innerHTML = "Distance: " + response['distance'].toString();
                button.innerHTML = "Button state: " + response['button'].toString();
                timestamp.innerHTML = "Timestamp: " + response['timestamp'].toString();
            }
            else{
                console.log("error")

                table_id.innerHTML = response['error'].toString();
                distance.innerHTML = "";
                button.innerHTML = "";
                timestamp.innerHTML = "";
            }
        });
}
 
// Get response for button criteria
function buttonState(){
    // Get the current time value from the text input box
    let button_state = document.getElementById('button_state').value;

    // This URL path is going to be the route defined in app.py
    let theURL= '/button/' + button_state;
    console.log(theURL);

    // Fetch is a Javascript function that sends a request to a server
    fetch(theURL)
        .then(response=>response.json()) // Convert response to JSON

        .then(function(response) {
            console.log(response)

            const table_id = document.getElementById("table_id");
            const distance = document.getElementById("distance"); 
            const button = document.getElementById("button"); 
            const timestamp = document.getElementById("timestamp");

            if (response['error'] == "no_error"){
                table_id.innerHTML = "ID: " + response['id'].toString();
                distance.innerHTML = "Distance: " + response['distance'].toString();
                button.innerHTML = "Button state: " + response['button'].toString();
                timestamp.innerHTML = "Timestamp: " + response['timestamp'].toString();
            }
            else{
                console.log("error")
                table_id.innerHTML = response['error'].toString();
                distance.innerHTML = "";
                button.innerHTML = "";
                timestamp.innerHTML = "";
            }
        });
}

// Get response for both distance and button criteria
function both(){
    // Get the current distance and time value from the text input box
    let selected_distance = document.getElementById('distance_range').value;
    let button_state = document.getElementById('button_state').value;

    // This URL path is going to be the route defined in app.py
    let theURL= '/both/' + selected_distance +'/' + button_state;
    console.log(theURL);

    // Fetch is a Javascript function that sends a request to a server
    fetch(theURL)
        .then(response=>response.json()) // Convert response to JSON

        .then(function(response) {
            console.log(response)

            const table_id = document.getElementById("table_id");
            const distance = document.getElementById("distance"); 
            const button = document.getElementById("button"); 
            const timestamp = document.getElementById("timestamp");

            if (response['error'] == "no_error"){
                table_id.innerHTML = "ID: " + response['id'].toString();
                distance.innerHTML = "Distance: " + response['distance'].toString();
                button.innerHTML = "Button state: " + response['button'].toString();
                timestamp.innerHTML = "Timestamp: " + response['timestamp'].toString();
            }
            else{
                console.log("error")
                table_id.innerHTML = response['error'].toString();
                distance.innerHTML = "";
                button.innerHTML = "";
                timestamp.innerHTML = "";
            }
        });
}

// Get response for starting data collecting from sensors
function start_recording(){

    let status = document.getElementById("status")
    status.innerHTML = "Collecting data now..."

    let theURL = '/record';
    fetch(theURL)
        .then(response=>response.json()) // Convert response to JSON
        .then(function(response) {
            console.log(response)
            if (response){
                status.innerHTML = response['msg'].toString();
            }
            else{
                console.log("error")
                status.innerHTML  = 'Error. Unable to record data from sensors...'
            }
    });
}
