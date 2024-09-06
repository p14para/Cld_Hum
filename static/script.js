document.addEventListener('DOMContentLoaded', function() {
    const temperatureElement = document.getElementById('temperature');
    const humidityElement = document.getElementById('humidity');
    const solenoid1Button = document.getElementById('solenoid1-button');
    const solenoid2Button = document.getElementById('solenoid2-button');
    const testButton = document.getElementById('test-button');

    let lastTemperature = null;
    let lastHumidity = null;

    function fetchData() {
        fetch('/data')
            .then(response => response.json())
            .then(data => {
                const temperature = data.temperature;
                const humidity = data.humidity;
                const solenoid1Status = data.solenoid_1_status;
                const solenoid2Status = data.solenoid_2_status;

                // Update temperature and humidity
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

                // Update solenoid 1 button status
                if (solenoid1Status === 1) {
                    solenoid1Button.textContent = 'Ανοικτή';
                } else {
                    solenoid1Button.textContent = 'Κλειστή';
                }

                // Update solenoid 2 button status
                if (solenoid2Status === 1) {
                    solenoid2Button.textContent = 'Ανοικτή';
                } else {
                    solenoid2Button.textContent = 'Κλειστή';
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    function toggleSolenoid1() {
        fetch('/toggle_solenoid_1', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                const status = data.solenoid_1_status;
                solenoid1Button.textContent = status === 1 ? 'Ανοικτή' : 'Κλειστή';
            })
            .catch(error => console.error('Error toggling solenoid 1:', error));
    }

    function toggleSolenoid2() {
        fetch('/toggle_solenoid_2', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                const status = data.solenoid_2_status;
                solenoid2Button.textContent = status === 1 ? 'Ανοικτή' : 'Κλειστή';
            })
            .catch(error => console.error('Error toggling solenoid 2:', error));
    }

    function test() {
        fetch('/test', { method: 'POST' })
            .then(response => response.json())
            .then(data => console.log('Test data logged successfully:', data))
            .catch(error => console.error('Error sending test request:', error));
    }

    solenoid1Button.addEventListener('click', toggleSolenoid1);
    solenoid2Button.addEventListener('click', toggleSolenoid2);
    testButton.addEventListener('click', test);

    // Fetch data every second
    // setInterval(fetchData, 1000);
});
