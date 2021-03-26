#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 17:02:27 2021

@author: kaydee
"""
#import flask
from flask import Flask, redirect, url_for, request, render_template, send_file, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os
from Alignment import ChangePerspective
from vcopy import Model as vModel
import json
#local changes

UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
PATH = ""



app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CORS_HEADERS'] = "Content-Type"
cors = CORS(app)

@app.route("/")
def home():
    return redirect(url_for("index"))


@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/results") 
def res():
    global PATH
    if PATH == "":
        # TODO : add custom error mesage - Invalid PATH
        return render_template("index.html")
    vmod= vModel(PATH)
    sudoku = vmod.predictions
    print(sudoku)
    suddict = {'vals':"".join(map(str,sudoku))}
    print(suddict,PATH)
    with open("templates/sudoku.json","w") as f:
       json.dump(suddict,f)
       print("JSON written")
    return render_template("review.html",preds = [suddict])
    
    
    

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
    
@app.route("/solve",methods=["GET","POST"])
def solve():
    if request.method == "POST":
        temp = ""
        for i in range(81):
            gres = request.form.get("c"+str(i))

            if gres == "":
                temp += "0"
            else:
                temp+=gres

        return render_template("solve.html",final_sudoku = [{"vals":temp}])
    return "fail"

@app.route("/api")
def api():
    return render_template("api.html")

@app.route("/api/get_json")
@cross_origin()
def gjson():
    return jsonify(id = "kaydee")

if __name__ == "__main__":
    app.run(debug=True)