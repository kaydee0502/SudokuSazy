#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:02:27 2021

@author: kaydee
"""
import flask
from flask import Flask, redirect, url_for, request, render_template, send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/output",methods=["GET","POST"])
def out():
    
    if request.method == "POST":
        img = request.files["img"]
        sfname = secure_filename(img.filename)
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], sfname))
        
        
        return "yes"
    return "no"
    



if __name__ == "__main__":
    app.run(debug = True)