from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Webhook endpoint to receive data from Milesight
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received webhook data:", data)
    return jsonify({"status": "success"}), 200

# Function to add a device using the Milesight API
def add_device():
    # API endpoint URL for adding a device
    url = "https://eu-openapi.milesight.com/device/openapi/v1.0/devices"  # Use the correct base URL

    # Your access token
    access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InllYXN0b25lLWRlZmF1bHQta2V5LWlkIn0.eyJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwic2NvcGUiOlsib3BlbmFwaSJdLCJjbGllbnRfZXh0Ijp7ImFwcF9pZCI6IjE4MjgzODg2NzExMjkxNTM1MzciLCJ1c2VyX2lkIjoiMTgyODM2NDg4ODQzNTEzMDM2OSIsInNlY3JldF92ZXJzaW9uIjoiMTcyNDc1NjgwMzY3NyJ9LCJleHAiOjE3MjUyOTkyNzMsImF1dGhvcml0aWVzIjpbIlJPTEVfQ0xJRU5UIl0sImp0aSI6ImZlYWZlZmU3LTIzYmUtNDc1NC1iNWU0LWNjYWI1Zjg5MDE4MSIsImNsaWVudF9pZCI6IjYyMTIyZjhmLTYyYTUtNDFhNy1hZDQzLTBlZmE0NTc4MjM4NCIsInRzIjoxNzI1Mjk1NjczNTMxfQ.MTEw6beOM37PmoeA7eq5VQ3vcTFuGYIKPl92e1ynVtCDUTC1MftPdLtG7ZCem1zjWR9LgGa1wfimFpcwJWiI2NAqiohE9eLiuKVNjoMeUDnwBsMXLjtnNEkFwlwzm_JZc3Y8ww4gTEETKNg7JThdTC4AGvaHGPptX8gIlEr-9qc"

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

    # Make the POST request to add the gateway
    response = requests.post(url, headers=headers, json=payload)

    # Check the response
    if response.status_code == 201:
        print("Gateway added successfully:", response.json())
    else:
        print("Failed to add gateway:", response.status_code, response.text)

if __name__ == '__main__':
    # Start Flask app
    app.run(debug=True, host='0.0.0.0')

    # Add the device when the application starts
    add_device()
