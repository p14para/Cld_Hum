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


# ------------------------------------------------------------
# UPDATE TO ADD POSTGRE 

# import eventlet
# eventlet.monkey_patch()

# from flask import Flask, request, jsonify, render_template
# from flask_socketio import SocketIO
# import logging
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://u6t8cp76dbgcpj:pc572ed8ec5d57bce5b4080bc59a8b0528c495097f1a19dd839fd0b6331e669f4@ccaml3dimis7eh.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d22ekdqd6mc7g9'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# socketio = SocketIO(app, async_mode='eventlet')

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Define your models here
# class DeviceData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     temperature = db.Column(db.Float)
#     humidity = db.Column(db.Float)
#     solenoid_1_status = db.Column(db.Integer, default=0)
#     solenoid_2_status = db.Column(db.Integer, default=0)

#     def __repr__(self):
#         return f'<DeviceData {self.id}>'

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

#         # Save to the database
#         device_data = DeviceData(
#             temperature=new_temperature,
#             humidity=new_humidity,
#             solenoid_1_status=new_solenoid_1_status,
#             solenoid_2_status=new_solenoid_2_status
#         )
#         db.session.add(device_data)
#         db.session.commit()

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


# --------------------------------------------------------
# FULL TRIGGER LOGIC WITH POSTGRESQL

import eventlet
eventlet.monkey_patch()

from flask import Flask, request, jsonify, render_template
from flask_socketio import SocketIO
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError

# Flask app setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://u6t8cp76dbgcpj:pc572ed8ec5d57bce5b4080bc59a8b0528c495097f1a19dd839fd0b6331e669f4@ccaml3dimis7eh.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d22ekdqd6mc7g9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup Flask-SQLAlchemy
db = SQLAlchemy(app)
socketio = SocketIO(app, async_mode='eventlet')

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define your models
class DeviceData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    solenoid_1_status = db.Column(db.Integer, nullable=False)
    solenoid_2_status = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

class Trigger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=True)
    temperature_comparison = db.Column(db.String, nullable=True)
    humidity = db.Column(db.Float, nullable=True)
    humidity_comparison = db.Column(db.String, nullable=True)
    time = db.Column(db.Time, nullable=True)
    solenoid = db.Column(db.String, nullable=True)
    action = db.Column(db.String, nullable=True)  # 'open' or 'close'

# Function to create tables
def create_tables():
    try:
        db.create_all()
        logger.info("Tables created successfully")
    except OperationalError as e:
        logger.error(f"An error occurred while creating tables: {e}")

# Call the function to create tables, ensure it's done manually if necessary
# create_tables()

# Global variables to store the latest device data
latest_data = {"temperature": None, "humidity": None}
solenoid_status = {"solenoid_1_status": 0, "solenoid_2_status": 0}

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    logger.info("Received data: %s", data)
    if data and 'data' in data and 'payload' in data['data']:
        payload = data['data']['payload']
        logger.info("Payload received: %s", payload)
        
        # Update the latest data
        new_temperature = payload.get('temperature')
        new_humidity = payload.get('humidity')
        logger.info("Updating temperature to %s and humidity to %s", new_temperature, new_humidity)
        
        latest_data['temperature'] = new_temperature
        latest_data['humidity'] = new_humidity
        
        # Update solenoid status only if present in payload
        new_solenoid_1_status = int(payload.get('solenoid_1_status', solenoid_status['solenoid_1_status']))
        new_solenoid_2_status = int(payload.get('solenoid_2_status', solenoid_status['solenoid_2_status']))
        
        logger.info("Updating solenoid_1_status to %d and solenoid_2_status to %d", new_solenoid_1_status, new_solenoid_2_status)
        
        solenoid_status['solenoid_1_status'] = new_solenoid_1_status
        solenoid_status['solenoid_2_status'] = new_solenoid_2_status

        logger.info("Updated latest_data: %s", latest_data)
        logger.info("Updated solenoid_status: %s", solenoid_status)

        # Emit updated data to all clients
        socketio.emit('update_data', {**latest_data, **solenoid_status})

        # Save to the database
        device_data = DeviceData(
            temperature=new_temperature,
            humidity=new_humidity,
            solenoid_1_status=new_solenoid_1_status,
            solenoid_2_status=new_solenoid_2_status
        )
        try:
            db.session.add(device_data)
            db.session.commit()
        except Exception as e:
            logger.error(f"An error occurred while saving to the database: {e}")
            db.session.rollback()

    return jsonify({"status": "success"}), 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle_solenoid_1', methods=['POST'])
def toggle_solenoid_1():
    solenoid_status['solenoid_1_status'] = 1 if solenoid_status['solenoid_1_status'] == 0 else 0
    logger.info("Toggled solenoid_1_status to %d", solenoid_status['solenoid_1_status'])
    socketio.emit('update_data', {**latest_data, **solenoid_status})
    return jsonify({"solenoid_1_status": solenoid_status['solenoid_1_status']})

@app.route('/toggle_solenoid_2', methods=['POST'])
def toggle_solenoid_2():
    solenoid_status['solenoid_2_status'] = 1 if solenoid_status['solenoid_2_status'] == 0 else 0
    logger.info("Toggled solenoid_2_status to %d", solenoid_status['solenoid_2_status'])
    socketio.emit('update_data', {**latest_data, **solenoid_status})
    return jsonify({"solenoid_2_status": solenoid_status['solenoid_2_status']})

@app.route('/test', methods=['POST'])
def test():
    # Log the current device status
    log_data = {"latest_data": latest_data, "solenoid_status": solenoid_status}
    logger.info("Current device status: %s", log_data)

    # Return success response
    return jsonify({"status": "success", "log_data": log_data}), 200

# New routes for the pages
@app.route('/conditions')
def conditions():
    return render_template('conditions.html')

@app.route('/compuland')
def compuland():
    return render_template('compuland.html')

@app.route('/devices')
def devices():
    return render_template('devices.html')

@app.route('/add_trigger', methods=['POST'])
def add_trigger():
    data = request.json
    logger.info("Adding trigger: %s", data)

    # Validate if trigger already exists
    existing_trigger = Trigger.query.filter_by(
        temperature=data.get('temperature'),
        temperature_comparison=data.get('temperature_comparison'),
        humidity=data.get('humidity'),
        humidity_comparison=data.get('humidity_comparison'),
        time=data.get('time'),
        solenoid=data.get('solenoid'),
        action=data.get('action')
    ).first()
    
    if existing_trigger:
        return jsonify({"success": False, "message": "Trigger already exists"}), 400

    trigger = Trigger(
        temperature=data.get('temperature'),
        temperature_comparison=data.get('temperature_comparison'),
        humidity=data.get('humidity'),
        humidity_comparison=data.get('humidity_comparison'),
        time=data.get('time'),
        solenoid=data.get('solenoid'),
        action=data.get('action')  # 'open' or 'close'
    )

    try:
        db.session.add(trigger)
        db.session.commit()
        return jsonify({"success": True, "id": trigger.id})
    except Exception as e:
        logger.error(f"An error occurred while adding trigger: {e}")
        db.session.rollback()
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/delete_trigger', methods=['POST'])
def delete_trigger():
    data = request.json
    trigger_id = data.get('id')
    logger.info("Deleting trigger with ID: %s", trigger_id)

    trigger = Trigger.query.get(trigger_id)
    if trigger:
        try:
            db.session.delete(trigger)
            db.session.commit()
            return jsonify({"success": True})
        except Exception as e:
            logger.error(f"An error occurred while deleting trigger: {e}")
            db.session.rollback()
            return jsonify({"success": False, "message": str(e)}), 500
    else:
        return jsonify({"success": False, "message": "Trigger not found"}), 404

@app.route('/get_triggers', methods=['GET'])
def get_triggers():
    triggers = Trigger.query.all()
    trigger_list = [
        {
            'id': trigger.id,
            'temperature': trigger.temperature,
            'temperature_comparison': trigger.temperature_comparison,
            'humidity': trigger.humidity,
            'humidity_comparison': trigger.humidity_comparison,
            'time': str(trigger.time) if trigger.time else '',
            'solenoid': trigger.solenoid,
            'action': trigger.action
        }
        for trigger in triggers
    ]
    logger.info("Fetching triggers")
    return jsonify({"triggers": trigger_list})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
# ----------------------------------------------------------