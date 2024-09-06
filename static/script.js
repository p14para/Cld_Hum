document.addEventListener('DOMContentLoaded', function() {
    const temperatureElement = document.getElementById('temperature');
    const humidityElement = document.getElementById('humidity');
    const solenoid1Button = document.getElementById('solenoid1-button');
    const solenoid2Button = document.getElementById('solenoid2-button');
    const testButton = document.getElementById('test-button');

    let lastTemperature = null;
    let lastHumidity = null;
    let isDebouncing = false; // For debounce

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
                solenoid1Button.textContent = solenoid1Status === 1 ? 'Κλειστή' : 'Ανοικτή';

                // Update solenoid 2 button status
                solenoid2Button.textContent = solenoid2Status === 1 ? 'Κλειστή' : 'Ανοικτή';
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    function debounce(func, wait) {
        return function(...args) {
            if (isDebouncing) return;
            isDebouncing = true;
            setTimeout(() => {
                func(...args);
                isDebouncing = false;
            }, wait);
        };
    }

    function toggleSolenoid1() {
        fetch('/toggle_solenoid_1', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                const status = data.solenoid_1_status;
                solenoid1Button.textContent = status === 1 ? 'Κλειστή' : 'Ανοικτή';
            })
            .catch(error => console.error('Error toggling solenoid 1:', error));
    }

    function toggleSolenoid2() {
        fetch('/toggle_solenoid_2', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                const status = data.solenoid_2_status;
                solenoid2Button.textContent = status === 1 ? 'Κλειστή' : 'Ανοικτή';
            })
            .catch(error => console.error('Error toggling solenoid 2:', error));
    }

    function test() {
        fetch('/test', { method: 'POST' })
            .then(response => response.json())
            .then(data => console.log('Test data logged successfully:', data))
            .catch(error => console.error('Error sending test request:', error));
    }

    // Debounced toggle functions
    const debouncedToggleSolenoid1 = debounce(toggleSolenoid1, 300);
    const debouncedToggleSolenoid2 = debounce(toggleSolenoid2, 300);

    solenoid1Button.addEventListener('click', debouncedToggleSolenoid1);
    solenoid2Button.addEventListener('click', debouncedToggleSolenoid2);
    testButton.addEventListener('click', test);

    // Fetch data every 5 seconds
    setInterval(fetchData, 5000);
});
