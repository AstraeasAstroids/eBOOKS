from flask import Flask, render_template, url_for,jsonify , send_from_directory
from flask_cors import CORS
import webbrowser
import threading
import os
# Create the Flask application
app = Flask(__name__)
# Allow other domains (e.g. your frontend) to request data from this server
CORS(app)


# Route: Home page
@app.route('/')
def home():
    return render_template('project.html')
# Define a GET endpoint at /images

# Route: /images - returns list of image URLs
@app.route('/images', methods=['GET'])


# This function will return a list of image URLs from the static/templates folder

def get_images():
    image_folder = os.path.join(app.static_folder, 'templates')
    if not os.path.exists(image_folder):
        return jsonify({"error": "Image folder does not exist"}), 404
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith('.jpg')]
    image_urls = [f'/static/templates/{img}' for img in image_files]
    return jsonify(image_urls)

    

# Route: /static/<path:filename> - serves static files


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # use Render's port or default to 5000
    app.run(host='0.0.0.0', port=port)

