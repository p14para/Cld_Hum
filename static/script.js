document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    // Function to fetch data from the server
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

    // Function to fetch triggers and update the table
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
            })
            .catch(error => console.error('Error fetching triggers:', error));
    }

    // Function to add a new trigger
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
            })
            .catch(error => console.error('Error adding trigger:', error));
    }

    // Function to delete a trigger
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
            })
            .catch(error => console.error('Error deleting trigger:', error));
    }

    // Form submission handler
    const triggerForm = document.getElementById('trigger-form');
    if (triggerForm) {
        triggerForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const data = {
                temperature: document.getElementById('temperature').value || null,
                temperature_comparison: document.getElementById('temperature_comparison').value || null,
                humidity: document.getElementById('humidity').value || null,
                humidity_comparison: document.getElementById('humidity_comparison').value || null,
                time: document.getElementById('time').value || null,
                solenoid: document.getElementById('solenoid').value || null
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

    // Initial fetches
    fetchData();
    fetchTriggers();
});
