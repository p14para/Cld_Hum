document.addEventListener('DOMContentLoaded', function() {
    const temperatureElement = document.getElementById('temperature');
    const humidityElement = document.getElementById('humidity');
    const solenoidButton = document.getElementById('solenoidButton');
    let solenoidStatus = 0;  // Default to closed

    let lastTemperature = null;
    let lastHumidity = null;

    function fetchData() {
        fetch('/data')
            .then(response => response.json())
            .then(data => {
                const temperature = data.temperature;
                const humidity = data.humidity;

                if (temperature !== null && temperature !== undefined) {
                    lastTemperature = temperature;
                    temperatureElement.textContent = temperature.toFixed(1);
                } else if (lastTemperature !== null) {
                    temperatureElement.textContent = lastTemperature.toFixed(1);
                }

                if (humidity !== null && humidity !== undefined) {
                    lastHumidity = humidity;
                    humidityElement.textContent = humidity.toFixed(1);
                } else if (lastHumidity !== null) {
                    humidityElement.textContent = lastHumidity.toFixed(1);
                }
                
                solenoidStatus = data.solenoid_1_status;
                solenoidButton.textContent = solenoidStatus === 1 ? 'Close' : 'Open';
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    // Toggle Solenoid status
    function toggleSolenoid() {
        solenoidStatus = solenoidStatus === 1 ? 0 : 1;
        solenoidButton.textContent = solenoidStatus === 1 ? 'Close' : 'Open';

        // Send new status to the server
        fetch('/toggle_solenoid', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ solenoid_1_status: solenoidStatus })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Solenoid status updated:', data);
        })
        .catch(error => console.error('Error updating solenoid status:', error));
    }

    // Fetch data every second
    // setInterval(fetchData, 1000);
});
