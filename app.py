from flask import Flask, request, jsonify
import requests
import subprocess
import threading

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received webhook data: {data}")
    response = requests.post('https://webhook.site/5966340c-fbfb-470e-ad66-ef392ea121e5', json=data)
    print(f"Response from webhook.site: {response.status_code} - {response.text}")
    return jsonify({'message': 'Webhook received and forwarded successfully!', 'data': data}), 200

def run_flask_app():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    curl_command = [
        'curl', '-X', 'POST', 'http://192.168.1.117:5000/webhook',
        '-H', 'Content-Type: application/json',
        '-d', '{"key1":"value1", "key2":"value2"}'
    ]

    try:
        subprocess.run(curl_command, check=True)
        print("Curl command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing curl command: {e}")
