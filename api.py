from flask import Flask, redirect, url_for, request, render_template, send_file, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os
from Alignment import ChangePerspective
from vcopy import Model as vModel
import json