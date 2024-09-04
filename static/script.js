function updateData() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('temperature').textContent = data.temperature !== null ? data.temperature : 'N/A';
            document.getElementById('humidity').textContent = data.humidity !== null ? data.humidity : 'N/A';
        })
        .catch(error => console.error('Error fetching data:', error));
}

// Update data every 5 seconds
setInterval(updateData, 5000);

// Initial data fetch
updateData();
