from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the URL to forward data to
FORWARD_URL = 'https://cldhum-5efb54746e98.herokuapp.com/'  # Update if needed

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received webhook data: {data}")

    # Forward the data to the specified URL
    try:
        response = requests.post(FORWARD_URL, json=data)
        print(f"Response from forward URL: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Error forwarding data: {e}")

    return jsonify({'message': 'Webhook received and forwarded successfully!', 'data': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
