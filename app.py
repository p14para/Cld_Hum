from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MILEIGHT_API_URL = 'https://eu-openapi.milesight.com'
ACCESS_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InllYXN0b25lLWRlZmF1bHQta2V5LWlkIn0.eyJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwic2NvcGUiOlsib3BlbmFwaSJdLCJjbGllbnRfZXh0Ijp7ImFwcF9pZCI6IjE4MjgzODg2NzExMjkxNTM1MzciLCJ1c2VyX2lkIjoiMTgyODM2NDg4ODQzNTEzMDM2OSIsInNlY3JldF92ZXJzaW9uIjoiMTcyNDc1NjgwMzY3NyJ9LCJleHAiOjE3MjUyNzA1NTgsImF1dGhvcml0aWVzIjpbIlJPTEVfQ0xJRU5UIl0sImp0aSI6ImYzYTc0NWYzLTc5NmUtNDg0Mi05YmFlLTc3OTBjYThjOGM0YyIsImNsaWVudF9pZCI6IjYyMTIyZjhmLTYyYTUtNDFhNy1hZDQzLTBlZmE0NTc4MjM4NCIsInRzIjoxNzI1MjY2OTU4NDgxfQ.ABWTaMIewhYK3jCl3MTRUJ7_qqJGR2Ec7iAOd4jyJ5XHwfn83VVAjtvYOTKSon5Nue7N1foQ0g9muWUlozkOX-VkjuMe4FyfzC1qkPsK5U7GVZ_tqdtJy0R0hGWwhyhSg1VkKiwHF-kn7A4lvsjqFh1Xxj8PlGeRXSY4AUusm_c'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Received webhook data: {data}")
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    response = requests.post(MILEIGHT_API_URL, json=data, headers=headers)
    print(f"Response from Milesight API: {response.status_code} - {response.text}")
    return jsonify({'message': 'Webhook received and forwarded successfully!', 'data': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
