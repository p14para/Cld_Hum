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
        if (temperature !== null && temperature !== undefined) {
            temperatureElement.textContent = temperature.toFixed(1);
        }

        if (humidity !== null && humidity !== undefined) {
            humidityElement.textContent = humidity.toFixed(1);
        }

        // Update solenoid 1 button status
        solenoid1Button.textContent = solenoid1Status === 1 ? 'Ανοικτή' : 'Κλειστή';

        // Update solenoid 2 button status
        solenoid2Button.textContent = solenoid2Status === 1 ? 'Ανοικτή' : 'Κλειστή';
    });

    function toggleSolenoid1() {
        fetch('/toggle_solenoid_1', { method: 'POST' })
            .then(response => response.json())
            .catch(error => console.error('Error toggling solenoid 1:', error));
    }

    function toggleSolenoid2() {
        fetch('/toggle_solenoid_2', { method: 'POST' })
            .then(response => response.json())
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
});
