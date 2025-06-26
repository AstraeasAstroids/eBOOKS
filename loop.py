import os

folder_path = './static/templates'

for filename in os.listdir(folder_path):
    if filename.lower().endswith('.jpg'):
        print(filename)