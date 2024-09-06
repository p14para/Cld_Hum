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
                }

                if (humidity !== null && humidity !== undefined) {
                    lastHumidity = humidity;
                    humidityElement.textContent = humidity.toFixed(1);
                }

                // Update solenoid button text based on status
                solenoidStatus = data.solenoid_1_status;
                solenoidButton.textContent = solenoidStatus === 1 ? 'Close' : 'Open';
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    // Toggle Solenoid status
    function toggleSolenoid() {
        const newStatus = solenoidStatus === 1 ? 0 : 1;

        fetch('/toggle_solenoid', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ solenoid_1_status: newStatus })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                solenoidStatus = newStatus;  // Update solenoid status locally
                solenoidButton.textContent = solenoidStatus === 1 ? 'Close' : 'Open';
                console.log('Solenoid status updated:', data);
            } else {
                console.error('Failed to update solenoid status');
            }
        })
        .catch(error => console.error('Error updating solenoid status:', error));
    }

    // Attach event listener to button
    solenoidButton.addEventListener('click', toggleSolenoid);

    // Fetch data every second
    // setInterval(fetchData, 1000);
});
