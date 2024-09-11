document.addEventListener('DOMContentLoaded', function() {
    const socket = new SockJS('/socket');
    const stompClient = Stomp.over(socket);

    stompClient.connect({}, function(frame) {
        stompClient.subscribe('/topic/update_data', function(message) {
            const data = JSON.parse(message.body);
            document.getElementById('temperature').innerText = data.temperature || 'N/A';
            document.getElementById('humidity').innerText = data.humidity || 'N/A';
            document.getElementById('solenoid_1_status').innerText = data.solenoid_1_status ? 'Ανοιχτό' : 'Κλειστό';
            document.getElementById('solenoid_2_status').innerText = data.solenoid_2_status ? 'Ανοιχτό' : 'Κλειστό';
        });
    });

    document.getElementById('toggle_solenoid_1').addEventListener('click', function() {
        fetch('/toggle_solenoid_1', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('solenoid_1_status').innerText = data.solenoid_1_status ? 'Ανοιχτό' : 'Κλειστό';
        });
    });

    document.getElementById('toggle_solenoid_2').addEventListener('click', function() {
        fetch('/toggle_solenoid_2', {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('solenoid_2_status').innerText = data.solenoid_2_status ? 'Ανοιχτό' : 'Κλειστό';
        });
    });
});
