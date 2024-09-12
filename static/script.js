const socket = io();

document.addEventListener('DOMContentLoaded', () => {
    // Initial fetch and update of device data
    function fetchData() {
        fetch('/data')
            .then(response => response.json())
            .then(data => {
                document.getElementById('temperature').innerText = data.temperature || 'N/A';
                document.getElementById('humidity').innerText = data.humidity || 'N/A';
                document.getElementById('solenoid_1_status').innerText = data.solenoid_1_status || 'N/A';
                document.getElementById('solenoid_2_status').innerText = data.solenoid_2_status || 'N/A';
            });
    }

    // Fetch triggers and update the table
    function fetchTriggers() {
        fetch('/get_triggers')
            .then(response => response.json())
            .then(data => {
                const triggers = data.triggers;
                const triggerTable = document.getElementById('trigger-table').getElementsByTagName('tbody')[0];
                triggerTable.innerHTML = ''; // Clear existing rows
                triggers.forEach(trigger => {
                    const row = triggerTable.insertRow();
                    row.innerHTML = `
                        <td>${trigger.id}</td>
                        <td>${trigger.temperature || '-'}</td>
                        <td>${trigger.temperature_comparison || '-'}</td>
                        <td>${trigger.humidity || '-'}</td>
                        <td>${trigger.humidity_comparison || '-'}</td>
                        <td>${trigger.time || '-'}</td>
                        <td>${trigger.solenoid || '-'}</td>
                        <td><button onclick="deleteTrigger(${trigger.id})">Διαγραφή</button></td>
                    `;
                });
            });
    }

    // Add a new trigger
    function addTrigger(data) {
        fetch('/add_trigger', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    fetchTriggers(); // Refresh triggers table
                    document.getElementById('trigger-form').reset(); // Reset form
                } else {
                    alert(`Σφάλμα: ${data.message}`);
                }
            });
    }

    // Delete a trigger by ID
    function deleteTrigger(id) {
        fetch('/delete_trigger', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ id })
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    fetchTriggers(); // Refresh triggers table
                } else {
                    alert(`Σφάλμα: ${data.message}`);
                }
            });
    }

    // Form submission handler
    const triggerForm = document.getElementById('trigger-form');
    if (triggerForm) {
        triggerForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const data = {
                temperature: document.getElementById('temperature').value,
                temperature_comparison: document.getElementById('temperature_comparison').value,
                humidity: document.getElementById('humidity').value,
                humidity_comparison: document.getElementById('humidity_comparison').value,
                time: document.getElementById('time').value,
                solenoid: document.getElementById('solenoid').value
            };
            addTrigger(data);
        });
    }

    // WebSocket event listener for real-time updates
    socket.on('update_data', function(data) {
        document.getElementById('temperature').innerText = data.temperature || 'N/A';
        document.getElementById('humidity').innerText = data.humidity || 'N/A';
        document.getElementById('solenoid_1_status').innerText = data.solenoid_1_status || 'N/A';
        document.getElementById('solenoid_2_status').innerText = data.solenoid_2_status || 'N/A';
    });

    // Initial fetch
    fetchData();
    fetchTriggers();
});
