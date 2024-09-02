from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL to forward data to (if applicable)
FORWARD_URL = 'https://console.milesight.com/application/settings/1828388671129153537'  # Update this if you need to forward data

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received webhook data: {data}")

    # Optionally forward the data to another endpoint
    if FORWARD_URL:
        try:
            response = requests.post(FORWARD_URL, json=data)
            print(f"Response from forward URL: {response.status_code} - {response.text}")
        except requests.RequestException as e:
            print(f"Error forwarding data: {e}")

    # Respond with a success message
    return jsonify({'message': 'Webhook received and processed successfully!', 'data': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
