from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Root route for basic connection test
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Milesight Gateway API"}), 200

# Webhook endpoint to receive data from Milesight
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    app.logger.info("Received webhook data: %s", data)
    return jsonify({"status": "success"}), 200

# Function to add a device using the Milesight API
def add_device():
    try:
        # API endpoint URL for adding a device
        url = "https://eu-openapi.milesight.com/device/openapi/v1.0/devices"

        # Your access token
        access_token = "your_access_token_here"

        # Headers
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
            "User-Agent": "OpenAPI"
        }

        # Payload with gateway details
        payload = {
            "snDevEUI": "6221E1734211",  # Replace with your gateway's snDevEUI
            "name": "UG65",  # Replace with your gateway name
            "description": "test",  # Replace with your gateway description
            "project": "cld"  # Replace with your project name
        }

        app.logger.info("Sending request to add device with payload: %s", payload)

        # Make the POST request to add the gateway
        response = requests.post(url, headers=headers, json=payload)

        # Check the response
        if response.status_code == 201:
            app.logger.info("Gateway added successfully: %s", response.json())
        else:
            app.logger.error("Failed to add gateway: %s %s", response.status_code, response.text)

    except Exception as e:
        app.logger.error("An error occurred: %s", str(e))

@app.route('/start', methods=['GET'])
def start():
    add_device()
    return jsonify({"status": "Device addition initiated"}), 200

if __name__ == '__main__':
    # Start Flask app
    app.run(debug=True, host='0.0.0.0')
