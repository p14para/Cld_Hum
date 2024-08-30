from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get JSON data sent by the webhook
    data = request.json
    print(f"Received webhook data: {data}")
    
    # Forward the data to the specified endpoint
    try:
        # Change this URL to the endpoint where you want to forward the data
        forward_url = 'https://cldhum-5efb54746e98.herokuapp.com/' 
        response = requests.post(forward_url, json=data)
        print(f"Response from forward URL: {response.status_code} - {response.text}")
    except requests.RequestException as e:
        print(f"Error forwarding data: {e}")
    
    # Respond back to the sender
    return jsonify({'message': 'Webhook received and forwarded successfully!', 'data': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
