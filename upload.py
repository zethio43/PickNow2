#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 16:37:20 2018

@author: earthz
"""

# import requests
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'img'
# CUTBG_FOLDER ='cbg'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def api(filename):
#     files = {'file': open(filename, 'rb')}
#     requests.post(url, files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # api(filename)
    return render_template('index2.html', image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("UPLOAD_FOLDER",filename)

# @app.route('')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(port='5000')
