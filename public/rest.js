function distance_range() {
    // Get the current value from the text input box
    let selected_distance = document.getElementById('distance_range');
    let distance_lower = selected_distance.options[selected_distance.selectedIndex].value;

    
    let id = distance_lower;
    // This URL path is going to be the route defined in app.py
    console.log(id);
    let theURL='/data/'+id;
    //This logger is just to keep track of the function call.
    //You can use such log messages to debug your code if you need.
    console.log("Making a RESTful request to the server!")
    // fetch is a Javascript function that sends a request to a server
    fetch(theURL)
        .then(response=>response.json()) // Convert response to JSON
        // Run the anonymous function on the received JSON response

        .then(function(response) {
            // Set the value of the img_src attribute of the img tag
            // to the value received from the server
            console.log(response)
            if (response['error'] == "no_error"){
                let distance = document.getElementById('distance') 
                distance.innerHTML = "Distance:" + response['distance'].toString();
                let timestamp = document.getElementById('timestamp') 
                timestamp.innerHTML = "TimeStamp:" + response['timestamp'].toString();
            }
            else{
                console.log("error")
                distance.innerHTML = response['error'].toString();
            }
        });
}
 
function time_range(){
    let selected_time = document.getElementById('time_range');
    let time_lower = selected_time.options[selected_time.selectedIndex].value;

    
    let id = time_lower;
    // This URL path is going to be the route defined in app.py
    console.log(id);
    let theURL='/data/'+id;
    //This logger is just to keep track of the function call.
    //You can use such log messages to debug your code if you need.
    console.log("Making a RESTful request to the server!")
    // fetch is a Javascript function that sends a request to a server
    fetch(theURL)
        .then(response=>response.json()) // Convert response to JSON
        // Run the anonymous function on the received JSON response

        .then(function(response) {
            // Set the value of the img_src attribute of the img tag
            // to the value received from the server
            console.log(response)
            if (response['error'] == "no_error"){
                let distance = document.getElementById('distance') 
                distance.innerHTML = "Distance:" + response['distance'].toString();
                let timestamp = document.getElementById('timestamp') 
                timestamp.innerHTML = "TimeStamp:" + response['timestamp'].toString();
            }
            else{
                console.log("error")
                distance.innerHTML = response['error'].toString();
            }
        });

}

function both(){
    let selected_time = document.getElementById('time_range');
    let time_lower = selected_time.options[selected_time.selectedIndex].value;

    let selected_distance = document.getElementById('distance_range');
    let distance_lower = selected_distance.options[selected_distance.selectedIndex].value;

    let id =  distance_lower+ time_lower ;
    console.log(id);
    // This URL path is going to be the route defined in app.py
    let theURL='/both/'+id;
    //This logger is just to keep track of the function call.
    //You can use such log messages to debug your code if you need.
    console.log("Making a RESTful request to the server!")
    // fetch is a Javascript function that sends a request to a server
    fetch(theURL)
        .then(response=>response.json()) // Convert response to JSON
        // Run the anonymous function on the received JSON response

        .then(function(response) {
            // Set the value of the img_src attribute of the img tag
            // to the value received from the server
            console.log(response)
            if (response['error'] == "no_error"){
                let distance = document.getElementById('distance') 
                distance.innerHTML = "Distance:" + response['distance'].toString();
                let timestamp = document.getElementById('timestamp') 
                timestamp.innerHTML = "TimeStamp:" + response['timestamp'].toString();
            }
            else{
                console.log("error")
                distance.innerHTML = response['error'].toString();
            }
        });
}