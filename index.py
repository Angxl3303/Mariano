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

@app.route('/manifest.json')
def respuesta2():
    return render_template('manifest.json')

@app.route('/regist_serviceWorker.js')
def respuesta3():
    return send_from_directory('templates', 'regist_serviceWorker.js', mimetype='application/javascript')

if __name__ == '__main__':
    app.run()
