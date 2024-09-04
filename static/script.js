// SCRIPT FOR SHOWING TEMPERATURE AND HUMIDITY

// document.addEventListener('DOMContentLoaded', function() {
//     const temperatureElement = document.getElementById('temperature');
//     const humidityElement = document.getElementById('humidity');

//     let lastTemperature = null;
//     let lastHumidity = null;

//     function fetchData() {
//         fetch('/data')
//             .then(response => response.json())
//             .then(data => {
//                 const temperature = data.temperature;
//                 const humidity = data.humidity;

//                 // Update temperature only if valid data is received
//                 if (temperature !== null && temperature !== undefined) {
//                     lastTemperature = temperature;
//                     temperatureElement.textContent = temperature;
//                 } else if (lastTemperature !== null) {
//                     temperatureElement.textContent = lastTemperature;
//                 }

//                 // Update humidity only if valid data is received
//                 if (humidity !== null && humidity !== undefined) {
//                     lastHumidity = humidity;
//                     humidityElement.textContent = humidity;
//                 } else if (lastHumidity !== null) {
//                     humidityElement.textContent = lastHumidity;
//                 }
//             })
//             .catch(error => console.error('Error fetching data:', error));
//     }

//     // Fetch data every second
//     setInterval(fetchData, 10000);
// });



// -----------------------------------------------------------------------------------------------------------------------------

document.addEventListener('DOMContentLoaded', function() {
    const temperatureElement = document.getElementById('temperature');
    const humidityElement = document.getElementById('humidity');

    let lastTemperature = null;
    let lastHumidity = null;

    function fetchData() {
        fetch('/data')
            .then(response => response.json())
            .then(data => {
                const temperature = data.temperature;
                const humidity = data.humidity;

                // Update temperature only if valid data is received
                if (temperature !== null && temperature !== undefined) {
                    lastTemperature = temperature;
                    temperatureElement.textContent = temperature.toFixed(1);
                } else if (lastTemperature !== null) {
                    temperatureElement.textContent = lastTemperature.toFixed(1);
                }

                // Update humidity only if valid data is received
                if (humidity !== null && humidity !== undefined) {
                    lastHumidity = humidity;
                    humidityElement.textContent = humidity.toFixed(1);
                } else if (lastHumidity !== null) {
                    humidityElement.textContent = lastHumidity.toFixed(1);
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    // Fetch data every second
    setInterval(fetchData, 1000);
});

