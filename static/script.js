document.addEventListener('DOMContentLoaded', function() {
    const temperatureElement = document.getElementById('temperature');
    const humidityElement = document.getElementById('humidity');
    const solenoid1Button = document.getElementById('solenoid1-button');
    const solenoid2Button = document.getElementById('solenoid2-button');
    const testButton = document.getElementById('test-button');

    const socket = io();

    socket.on('update_data', function(data) {
        const temperature = data.temperature;
        const humidity = data.humidity;
        const solenoid1Status = data.solenoid_1_status;
        const solenoid2Status = data.solenoid_2_status;

        // Update temperature and humidity
        temperatureElement.textContent = temperature !== null ? temperature.toFixed(1) : 'N/A';
        humidityElement.textContent = humidity !== null ? humidity.toFixed(1) : 'N/A';

        // Update solenoid 1 button status
        solenoid1Button.textContent = solenoid1Status === 1 ? 'Κλειστή' : 'Ανοικτή';

        // Update solenoid 2 button status
        solenoid2Button.textContent = solenoid2Status === 1 ? 'Κλειστή' : 'Ανοικτή';
    });

    solenoid1Button.addEventListener('click', function() {
        fetch('/toggle_solenoid_1', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                const status = data.solenoid_1_status;
                solenoid1Button.textContent = status === 1 ? 'Κλειστή' : 'Ανοικτή';
            })
            .catch(error => console.error('Error toggling solenoid 1:', error));
    });

    solenoid2Button.addEventListener('click', function() {
        fetch('/toggle_solenoid_2', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                const status = data.solenoid_2_status;
                solenoid2Button.textContent = status === 1 ? 'Κλειστή' : 'Ανοικτή';
            })
            .catch(error => console.error('Error toggling solenoid 2:', error));
    });

    testButton.addEventListener('click', function() {
        fetch('/test', { method: 'POST' })
            .then(response => response.json())
            .then(data => console.log('Test data logged successfully:', data))
            .catch(error => console.error('Error sending test request:', error));
    });
});
