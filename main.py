from flask import Flask, request, jsonify 
# from flask import render_template 
  
# # creates a Flask application 
# app = Flask(__name__) 
  
  
# @app.route("/") 
# def hello(): 
#     message = "Test"
#     return render_template('index.html',  
#                            message=message) 
  
# # run the application 
# if __name__ == "__main__": 
#     app.run(debug=True)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get JSON data sent by the webhook
    data = request.json

    # Print the data for debugging
    print(f"Received webhook data: {data}")

    # Process the data (you can add your logic here)
    # For now, we'll just respond with a success message
    return jsonify({'message': 'Webhook received successfully!', 'data': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)