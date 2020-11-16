"""Initialize Flask pre-integrated HTTP + WSGI ('local') server (port 5000).

Defines the 'views' for each 'routes'.
"""

from flask import Flask, render_template, jsonify, request

from grandPyApp.main import Main

app = Flask(__name__) # name the WSGI application : "app"

@app.route('/')
@app.route('/index/')
def index():
    """Directs to index page."""
    return render_template("index.html") # TC

@app.route('/api/getAnswer', methods = ['POST'])
def getAnswer():
    """ 
    In : user question (string)
    Act : Send it to main class. 
    Out : Return results (in json).
    """
    question_send = request.form['question']

    reponse = Main(question_send)

    print('\nin : ', question_send) #TC
    
    out = jsonify({
        'answer' : question_send,
        'geo_coord_results' : reponse.geo_coord_results,
        'geo_adress_results' : reponse.geo_adress_results,
        'wiki_results' : reponse.wiki_results,
    })  

    print('out : ', out) #TC

    return out