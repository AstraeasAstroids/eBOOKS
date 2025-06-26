from flask import Flask, render_template, url_for
import webbrowser
import threading
import os


app = Flask(__name__)

@app.route('/')
def home():
    image_folder = os.path.join(app.static_folder, 'templates')
    image_files = [f for f in os.listdir(image_folder) if f.lower().endswith('.jpg')]
    image_urls = [url_for('static',filename=f'templates/{img}') for img in image_files]

    return render_template('project.html', images=image_urls)

def open_browser():
    webbrowser.open_new("https//127.0.0.1:5000/")

if __name__ == '__main__':
    threading.Timer(1.5, open_browser).start()
    app.run(debug=True)