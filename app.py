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

from flask import Flask, request, jsonify, render_template
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global variables to store the latest device data
latest_data = {"temperature": None, "humidity": None}

# Global variables to store the solenoid statuses
solenoid_status = {"solenoid_1_status": 0, "solenoid_2_status": 0}

# Webhook endpoint to receive data from devices
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    logger.info("Received data: %s", data)

    # Extract solenoid status and other data
    if data and 'data' in data and 'payload' in data['data']:
        payload = data['data']['payload']
        solenoid_status['solenoid_1_status'] = int(payload.get('solenoid_1_status', 0))
        solenoid_status['solenoid_2_status'] = int(payload.get('solenoid_2_status', 0))
        latest_data['temperature'] = payload.get('temperature')
        latest_data['humidity'] = payload.get('humidity')

    return jsonify({"status": "success"}), 200

# Endpoint to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to get the latest temperature, humidity, and solenoid statuses
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(latest_data | solenoid_status)

# Endpoint to toggle solenoid 1 status
@app.route('/toggle_solenoid_1', methods=['POST'])
def toggle_solenoid_1():
    solenoid_status['solenoid_1_status'] = 1 if solenoid_status['solenoid_1_status'] == 0 else 0
    return jsonify({"solenoid_1_status": solenoid_status['solenoid_1_status']})

# Endpoint to toggle solenoid 2 status
@app.route('/toggle_solenoid_2', methods=['POST'])
def toggle_solenoid_2():
    solenoid_status['solenoid_2_status'] = 1 if solenoid_status['solenoid_2_status'] == 0 else 0
    return jsonify({"solenoid_2_status": solenoid_status['solenoid_2_status']})

# Endpoint to log the current device status
@app.route('/test', methods=['POST'])
def test():
    logger.info("Current device status: %s", {"latest_data": latest_data, "solenoid_status": solenoid_status})
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
