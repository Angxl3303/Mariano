from flask import Flask, render_template, send_from_directory
from random import *

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/click')
def respuesta():
    rango = range(1,50)
    rango2 = range(50,99)
    rango3 = range(99,101)
    numero = randint(1,100)
    if numero in rango:
        return "<h1>Si</h1>"
    elif numero in rango2:
        return "<h1>No</h1>"
    elif numero in rango3:
        return "<h1>Revivan Yugoslavia</h1>"

def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)
    
