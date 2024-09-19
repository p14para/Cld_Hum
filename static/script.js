document.addEventListener('DOMContentLoaded', function() {
    const socket = io();

    // Elements for the dashboard
    const temperatureElement = document.getElementById('temperature');
    const humidityElement = document.getElementById('humidity');
    const solenoid1Button = document.getElementById('solenoid1-button');
    const solenoid2Button = document.getElementById('solenoid2-button');
    const testButton = document.getElementById('test-button');

    // Elements for the conditions page
    const triggerForm = document.getElementById('trigger-form');
    const triggerList = document.getElementById('trigger-list');

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

    // Handle condition form submission
    if (triggerForm) {
        triggerForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            
            const formData = new FormData(triggerForm);
            const data = Object.fromEntries(formData.entries());

            // Add action to handle solenoid actions
            const solenoidAction = data['solenoid-action'];
            let solenoid;
            if (solenoidAction) {
                solenoid = solenoidAction.split('_')[1];
                data['solenoid'] = solenoid;
                data['action'] = solenoidAction.split('_')[0]; // 'open' or 'close'
            }

            try {
                const response = await fetch('/add_trigger', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                if (result.success) {
                    alert('Συνθήκη προστέθηκε επιτυχώς!');
                    loadTriggers();
                } else {
                    alert('Σφάλμα κατά την προσθήκη συνθήκης: ' + result.message);
                }
            } catch (error) {
                console.error('Error adding trigger:', error);
            }
        });
    }

    // Load active triggers
    async function loadTriggers() {
        try {
            const response = await fetch('/get_triggers');
            const data = await response.json();

            triggerList.innerHTML = '';

            data.triggers.forEach(trigger => {
                const li = document.createElement('li');
                li.textContent = `Συνθήκη ${trigger.id}: Θερμοκρασία ${trigger.temperature_comparison} ${trigger.temperature}, Υγρασία ${trigger.humidity_comparison} ${trigger.humidity}, Ώρα ${trigger.time || 'N/A'}, Σολενοειδές ${trigger.solenoid}`;

                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Διαγραφή';
                deleteButton.addEventListener('click', () => deleteTrigger(trigger.id));

                li.appendChild(deleteButton);
                triggerList.appendChild(li);
            });
        } catch (error) {
            console.error('Error loading triggers:', error);
        }
    }

    // Delete trigger
    async function deleteTrigger(id) {
        try {
            const response = await fetch('/delete_trigger', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ id })
            });

            const result = await response.json();

            if (result.success) {
                alert('Συνθήκη διαγράφηκε επιτυχώς!');
                loadTriggers();
            } else {
                alert('Σφάλμα κατά τη διαγραφή συνθήκης: ' + result.message);
            }
        } catch (error) {
            console.error('Error deleting trigger:', error);
        }
    }

    // Load triggers on page load
    if (triggerList) {
        loadTriggers();
    }
});
