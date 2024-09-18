document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    function updateDashboard(data) {
        document.getElementById('temperature').textContent = data.temperature ? `${data.temperature} °C` : 'Δεν διαθέσιμο';
        document.getElementById('humidity').textContent = data.humidity ? `${data.humidity} %` : 'Δεν διαθέσιμο';
        document.getElementById('solenoid_1_status').textContent = data.solenoid_1_status === 1 ? 'Ανοιχτό' : 'Κλειστό';
        document.getElementById('solenoid_2_status').textContent = data.solenoid_2_status === 1 ? 'Ανοιχτό' : 'Κλειστό';
    }

    socket.on('update_data', (data) => {
        updateDashboard(data);
    });

    document.getElementById('toggleSolenoid1').addEventListener('click', () => {
        fetch('/toggle_solenoid_1', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                updateDashboard(data);
            });
    });

    document.getElementById('toggleSolenoid2').addEventListener('click', () => {
        fetch('/toggle_solenoid_2', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                updateDashboard(data);
            });
    });

    document.getElementById('testButton').addEventListener('click', () => {
        fetch('/test', { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                console.log('Test response:', data);
            });
    });
});
