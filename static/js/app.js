async function fetchData() {
    try {
        const response = await fetch('/data');
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        const data = await response.json();
        
        // Check if the data contains the expected fields
        if (data && data.temperature !== undefined && data.humidity !== undefined) {
            document.getElementById('temperature').textContent = `Temperature: ${data.temperature !== null ? data.temperature : 'N/A'} °C`;
            document.getElementById('humidity').textContent = `Humidity: ${data.humidity !== null ? data.humidity : 'N/A'} %`;
        } else {
            console.warn('Unexpected data format:', data);
        }
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Fetch data every 5 seconds
setInterval(fetchData, 5000);

// Initial fetch when page loads
window.onload = fetchData;
