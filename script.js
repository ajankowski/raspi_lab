$(document).ready(function doPoll() {
    $.getJSON('http://localhost:5000/sensor_data', 
    function (data) {
        console.log(data);

        $('#temp').html(data.temp);
        setTimeout(doPoll, 5000);
    });
});

