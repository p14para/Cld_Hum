#CODE TO ADD DEVICES TO THE APPLICATION ON DEVELOPER PLATFORM - NEED TO CHANGE TOKENS AND INFORMATIONS

# from flask import Flask, request, jsonify
# import requests
# import logging

# app = Flask(__name__)

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)
# app.logger.setLevel(logging.DEBUG)

# # Webhook endpoint to receive data from Milesight
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.json
#     app.logger.info("Received webhook data: %s", data)
#     return jsonify({"status": "success"}), 200

# # Function to add a device using the Milesight API
# def add_device():
#     try:
#         # API endpoint URL for adding a device
#         url = "https://eu-openapi.milesight.com/device/openapi/v1.0/devices"

#         # Your access token (ensure it's correct and not expired)
#         access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InllYXN0b25lLWRlZmF1bHQta2V5LWlkIn0.eyJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwic2NvcGUiOlsib3BlbmFwaSJdLCJjbGllbnRfZXh0Ijp7ImFwcF9pZCI6IjE4MjgzODg2NzExMjkxNTM1MzciLCJ1c2VyX2lkIjoiMTgyODM2NDg4ODQzNTEzMDM2OSIsInNlY3JldF92ZXJzaW9uIjoiMTcyNDc1NjgwMzY3NyJ9LCJleHAiOjE3MjU2MTE5MDEsImF1dGhvcml0aWVzIjpbIlJPTEVfQ0xJRU5UIl0sImp0aSI6IjNlNTAzNzg0LTgxZmYtNDhjMi04ZWRkLWE5ZjMyNDE2YjZkMSIsImNsaWVudF9pZCI6IjYyMTIyZjhmLTYyYTUtNDFhNy1hZDQzLTBlZmE0NTc4MjM4NCIsInRzIjoxNzI1NjA4MzAxMTY0fQ.TnFQlOpPdZNBvQGml1O-vljEm8-_FprulLhEXgmZaFoMCaYuzMIi1tvl953LKlgnoXEjRbkR2SCkUXjZaU7DNgEXimOz6Ium-XX-H2aQ7NmTJFhAFKcPlSms0lKnUKFqQqsoiGTRCQV7ClknG4FjLXkck9P1qv_ZPa44bR5aJSs"  # Ensure this token is valid and current

#         # Headers
#         headers = {
#             "Authorization": f"Bearer {access_token}",
#             "Content-Type": "application/json",
#             "User-Agent": "OpenAPI"
#         }

#         # Payload with gateway details
#         payload = {
#             "snDevEUI": "6460D32799600014",  # Replace with your gateway's snDevEUI
#             "name": "UC512-DI",  # Replace with your gateway name
#             "description": "valve",  # Replace with your gateway description
#             "project": "cld"  # Replace with your project name
#         }

#         app.logger.info("Sending request to add device with payload: %s", payload)

#         # Make the POST request to add the gateway
#         response = requests.post(url, headers=headers, json=payload)

#         # Log the full response
#         app.logger.debug("Response status code: %s", response.status_code)
#         app.logger.debug("Response body: %s", response.text)

#         # Check the response
#         if response.status_code == 201:
#             app.logger.info("Gateway added successfully: %s", response.json())
#         else:
#             app.logger.error("Failed to add gateway: %s %s", response.status_code, response.text)

#     except Exception as e:
#         app.logger.error("An error occurred: %s", str(e))

# @app.route('/start', methods=['GET'])
# def start():
#     app.logger.info("Starting device addition process")
#     add_device()
#     return jsonify({"status": "Device addition initiated"}), 200

# if __name__ == '__main__':
#     # Start Flask app
#     app.run(debug=True, host='0.0.0.0')



#--------------------------------------------------------------------------------------------------------------------------------



#CODE TO SHOW DATA FROM DEVICES TO HEROKU CLI heroku logs --tail --app=cldhum

# from flask import Flask, request, jsonify
# import logging

# app = Flask(__name__)

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Webhook endpoint to receive data from devices
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.json
#     logger.info("Received data: %s", data)
#     return jsonify({"status": "success"}), 200

# if __name__ == '__main__':
#     # Start Flask app
#     app.run(debug=True, host='0.0.0.0')

#-------------------------------------------------------------------------------------------------------------------


#GRAPHICALLY SHOW THE LOG FOR TEMPERATURE AND HUMIDITY IN THE HTML PAGE

# import eventlet
# eventlet.monkey_patch()

# from flask import Flask, request, jsonify, render_template
# from flask_socketio import SocketIO
# import logging

# app = Flask(__name__)
# socketio = SocketIO(app, async_mode='eventlet')

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Global variables to store the latest device data
# latest_data = {"temperature": None, "humidity": None}
# solenoid_status = {"solenoid_1_status": 0, "solenoid_2_status": 0}

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.json
#     logger.info("Received data: %s", data)
#     if data and 'data' in data and 'payload' in data['data']:
#         payload = data['data']['payload']
#         logger.info("Payload received: %s", payload)
        
#         # Update the latest data
#         new_temperature = payload.get('temperature')
#         new_humidity = payload.get('humidity')
#         logger.info("Updating temperature to %s and humidity to %s", new_temperature, new_humidity)
        
#         latest_data['temperature'] = new_temperature
#         latest_data['humidity'] = new_humidity
        
#         # Update solenoid status only if present in payload
#         new_solenoid_1_status = int(payload.get('solenoid_1_status', solenoid_status['solenoid_1_status']))
#         new_solenoid_2_status = int(payload.get('solenoid_2_status', solenoid_status['solenoid_2_status']))
        
#         logger.info("Updating solenoid_1_status to %d and solenoid_2_status to %d", new_solenoid_1_status, new_solenoid_2_status)
        
#         solenoid_status['solenoid_1_status'] = new_solenoid_1_status
#         solenoid_status['solenoid_2_status'] = new_solenoid_2_status

#         logger.info("Updated latest_data: %s", latest_data)
#         logger.info("Updated solenoid_status: %s", solenoid_status)

#         # Emit updated data to all clients
#         socketio.emit('update_data', {**latest_data, **solenoid_status})

#     return jsonify({"status": "success"}), 200

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/toggle_solenoid_1', methods=['POST'])
# def toggle_solenoid_1():
#     solenoid_status['solenoid_1_status'] = 1 if solenoid_status['solenoid_1_status'] == 0 else 0
#     logger.info("Toggled solenoid_1_status to %d", solenoid_status['solenoid_1_status'])
#     socketio.emit('update_data', {**latest_data, **solenoid_status})
#     return jsonify({"solenoid_1_status": solenoid_status['solenoid_1_status']})

# @app.route('/toggle_solenoid_2', methods=['POST'])
# def toggle_solenoid_2():
#     solenoid_status['solenoid_2_status'] = 1 if solenoid_status['solenoid_2_status'] == 0 else 0
#     logger.info("Toggled solenoid_2_status to %d", solenoid_status['solenoid_2_status'])
#     socketio.emit('update_data', {**latest_data, **solenoid_status})
#     return jsonify({"solenoid_2_status": solenoid_status['solenoid_2_status']})

# @app.route('/test', methods=['POST'])
# def test():
#     # Log the current device status
#     log_data = {"latest_data": latest_data, "solenoid_status": solenoid_status}
#     logger.info("Current device status: %s", log_data)

#     # Return success response
#     return jsonify({"status": "success", "log_data": log_data}), 200

# # New routes for the empty pages
# @app.route('/conditions')
# def conditions():
#     return render_template('conditions.html')

# @app.route('/compuland')
# def compuland():
#     return render_template('compuland.html')

# @app.route('/devices')
# def devices():
#     return render_template('devices.html')

# if __name__ == '__main__':
#     socketio.run(app, debug=True, host='0.0.0.0')


from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
import time
from datetime import datetime
import threading
import eventlet

# Enable WebSocket support
eventlet.monkey_patch()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

# Simulate the latest device data
latest_data = {
    'temperature': 25.0,
    'humidity': 60.0
}

# Solenoid status
solenoid_status = {
    'solenoid_1_status': 0,
    'solenoid_2_status': 0
}

# Store triggers
triggers = {
    "time": [],
    "temperature": [],
    "humidity": []
}

# Route to serve the conditions page
@app.route('/conditions')
def conditions():
    return render_template('conditions.html')

# Routes to handle trigger submissions
@app.route('/add_time_trigger', methods=['POST'])
def add_time_trigger():
    data = request.json
    time_trigger = {
        "time": data['time'],
        "solenoid": data['solenoid'],
        "action": data['action']
    }
    triggers['time'].append(time_trigger)
    return jsonify({"status": "Time trigger added", "trigger": time_trigger})

@app.route('/add_temperature_trigger', methods=['POST'])
def add_temperature_trigger():
    data = request.json
    temperature_trigger = {
        "temperature": float(data['temperature']),
        "solenoid": data['solenoid'],
        "action": data['action']
    }
    triggers['temperature'].append(temperature_trigger)
    return jsonify({"status": "Temperature trigger added", "trigger": temperature_trigger})

@app.route('/add_humidity_trigger', methods=['POST'])
def add_humidity_trigger():
    data = request.json
    humidity_trigger = {
        "humidity": float(data['humidity']),
        "solenoid": data['solenoid'],
        "action": data['action']
    }
    triggers['humidity'].append(humidity_trigger)
    return jsonify({"status": "Humidity trigger added", "trigger": humidity_trigger})

# WebSocket route to send the current solenoid status
@socketio.on('connect')
def handle_connect():
    socketio.emit('solenoid_status_update', solenoid_status)

# Function to check triggers
def check_triggers():
    while True:
        current_time = datetime.now().strftime('%H:%M')
        
        # Check time-based triggers
        for trigger in triggers['time']:
            if trigger['time'] == current_time:
                control_solenoid(trigger['solenoid'], trigger['action'])
        
        # Check temperature-based triggers
        for trigger in triggers['temperature']:
            if latest_data['temperature'] is not None and latest_data['temperature'] >= trigger['temperature']:
                control_solenoid(trigger['solenoid'], trigger['action'])
        
        # Check humidity-based triggers
        for trigger in triggers['humidity']:
            if latest_data['humidity'] is not None and latest_data['humidity'] >= trigger['humidity']:
                control_solenoid(trigger['solenoid'], trigger['action'])
        
        eventlet.sleep(60)  # Check every minute

# Function to control solenoids
def control_solenoid(solenoid, action):
    if solenoid == "1":
        solenoid_status['solenoid_1_status'] = 1 if action == 'open' else 0
    elif solenoid == "2":
        solenoid_status['solenoid_2_status'] = 1 if action == 'open' else 0

    # Emit the status update to the frontend
    socketio.emit('solenoid_status_update', solenoid_status)

# Start checking triggers in a separate thread
trigger_thread = threading.Thread(target=check_triggers)
trigger_thread.start()

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0')

