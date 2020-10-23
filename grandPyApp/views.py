"""Initialize Flask pre-integrated HTTP + WSGI ('local') server (port 5000).

Defines the 'views' for each 'routes'.
"""

from flask import Flask, render_template


app = Flask(__name__) # name the WSGI application : "app"

@app.route('/') # a "view"
@app.route('/index/') # don't forget "/" at the end
def index():
    return render_template("index.html")


@app.route('/result/')
def result():
    return render_template("result.html")


