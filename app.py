from flask import Flask, render_template, url_for,jsonify , send_from_directory
from flask_cors import CORS
import webbrowser
import threading
import os
# Create the Flask application
app = Flask(__name__)
# Allow other domains (e.g. your frontend) to request data from this server
CORS(app)
# Define a GET endpoint at /images
@app.route('/images', methods=['GET'])



def get_images():
    # Build the path to the folder where your images live
    image_folder = os.path.join(app.static_folder, 'templates')
    # If that folder isn't there, return a 404 error in JSON form
    if not os.path.exists(image_folder):
        return jsonify({"error": "Image folder does not exist"}), 404
    # List out every file ending in .jpg in the folder
    image_files = [
        f for f in os.listdir(image_folder) 
        if f.lower().endswith('.jpg')
        ]
    # Turn each filename into a URL the client can fetch
    image_urls = [
        f'/static/templates/{img}' 
        for img in image_files
    ]
    # Send the list of URLs back as JSON
    return jsonify(image_urls)
# If you run this script directly (python your_app.py), start Flask’s dev server

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('project.html')
# If you want to run this app in a browser, open it automatically
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # use Render's port or default to 5000
    app.run(host='0.0.0.0', port=port)

