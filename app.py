#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:02:27 2021

@author: kaydee
"""
#import flask
from flask import Flask, redirect, url_for, request, render_template, send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os
from Alignment import ChangePerspective
#from vcopy import Model as vModel

UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
PATH = ""

app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return redirect(url_for("index"))


@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/results") 
def res():
    global PATH
    vM1= vModel(PATH)
    sudoku = vM1.predictions
    return str(sudoku)
    
    
    

@app.route("/output",methods=["GET","POST"])
def out():
    global PATH
    cpers = ChangePerspective()
    if request.method == "POST":
        img = request.files["img"]
        sfname = secure_filename(img.filename)
        img.save(app.config['UPLOAD_FOLDER']+sfname)
        fpath = os.path.join(app.config['UPLOAD_FOLDER'],sfname)
        
        print(sfname,app.config['UPLOAD_FOLDER'],fpath)
        cpers.readim(fpath,sfname)
        edited_sfname ="edited_"+sfname
        rel_image_path = "../static/images/"  
        PATH =os.path.join(app.config['UPLOAD_FOLDER'],edited_sfname)
        
        return render_template("result.html",inp = rel_image_path+sfname, out = rel_image_path+edited_sfname)
    return "no"
    



if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0")