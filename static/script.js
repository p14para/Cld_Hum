document.addEventListener('DOMContentLoaded', function() {
    const socket = io();

    // Elements for the dashboard
    const temperatureElement = document.getElementById('temperature');
    const humidityElement = document.getElementById('humidity');
    const solenoid1Button = document.getElementById('solenoid1-button');
    const solenoid2Button = document.getElementById('solenoid2-button');
    const testButton = document.getElementById('test-button');

    // Update the dashboard with new data
    socket.on('update_data', function(data) {
        if (temperatureElement && data.temperature !== null) {
            temperatureElement.textContent = data.temperature;
        }
        if (humidityElement && data.humidity !== null) {
            humidityElement.textContent = data.humidity;
        }
        if (solenoid1Button && data.solenoid_1_status !== undefined) {
            solenoid1Button.textContent = data.solenoid_1_status === 1 ? 'Ανοικτή' : 'Κλειστή';
        }
        if (solenoid2Button && data.solenoid_2_status !== undefined) {
            solenoid2Button.textContent = data.solenoid_2_status === 1 ? 'Ανοικτή' : 'Κλειστή';
        }
    });

    // Toggle solenoid 1 status
    if (solenoid1Button) {
        solenoid1Button.addEventListener('click', function() {
            fetch('/toggle_solenoid_1', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    solenoid1Button.textContent = data.solenoid_1_status === 1 ? 'Ανοικτή' : 'Κλειστή';
                })
                .catch(error => console.error('Error toggling solenoid 1:', error));
        });
    }

    // Toggle solenoid 2 status
    if (solenoid2Button) {
        solenoid2Button.addEventListener('click', function() {
            fetch('/toggle_solenoid_2', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    solenoid2Button.textContent = data.solenoid_2_status === 1 ? 'Ανοικτή' : 'Κλειστή';
                })
                .catch(error => console.error('Error toggling solenoid 2:', error));
        });
    }

    // Test button
    if (testButton) {
        testButton.addEventListener('click', function() {
            fetch('/test', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    console.log('Test data logged successfully:', data.log_data);
                })
                .catch(error => console.error('Error sending test request:', error));
        });
    }
});
