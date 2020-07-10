from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template


app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

@app.route('/')
def hello_world():
    return render_template('home.html')
