"""Initialize Flask pre-integrated HTTP + WSGI ('local') server (port 5000).

Defines the 'views' for each 'routes'.
"""
import os 
from flask import Flask, render_template, jsonify, request

from .main import Main
from .settings import MAPBOX_API_KEY

app = Flask(__name__) # name the WSGI application : "app"

@app.route('/')
def index():
    """Directs to index page."""
    return render_template("template.html", ACCESS_TOKEN=MAPBOX_API_KEY) # TC

@app.route('/api/getAnswer', methods = ['POST'])
def getAnswer():
    """ 
    In : user question (string)
    Act : Send it to main class. 
    Out : Return results (in json).
    """
    question_send = request.form['question']

    response = Main(question_send)

    print('\nin : ', question_send) #TC
    
    out = jsonify({
        'answer' : question_send,
        'bonus_message' : response.bonus_message,
        'geo_coord_results' : response.geo_coord_results,
        'geo_adress_results' : response.geo_adress_results,
        'wiki_results' : response.wiki_results,
        'geo_fail' : response.geo_fail,
        'wiki_fail' : response.wiki_fail
    })  

    print('out : ', out) #TC

    return out