"""Initialize Flask pre-integrated HTTP + WSGI ('local') server (port 5000).

Defines the 'views' for each 'routes'.
"""

from flask import Flask, render_template, jsonify, request


app = Flask(__name__) # name the WSGI application : "app"

@app.route('/') # a "view"
@app.route('/index/') # don't forget "/" at the end
def index():
    return render_template("index.html") # TC

@app.route('/api/getAnswer', methods = ['POST'])
def getAnswer():
    # directs to the files until get result (formatable in json)
    question_send = request.form['question']
    # a = $_POST['question']
    print('\n in : ', question_send) #TC
    
    out = jsonify({
        'answer':question_send
    })  
    print('out : ', out) #TC
    print('out_type : ', type(out),'\n') #TC
    return out

    # return jsonify({
    #     'questionAlpha' : a
    # }) 



# https://stackoverflow.com/questions/3477333/what-is-the-difference-between-post-and-get/3477374#3477374
# https://sutterlity.gitbooks.io/apprendre-jquery/content/ajax.html