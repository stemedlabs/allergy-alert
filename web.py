from flask import Flask, request, jsonify
import requests
from flask import render_template

app = Flask(__name__)

# getPollenCount

@app.route('/pollencount/')
@app.route('/pollencount/<name>')
def hello(name=None):
    return render_template('pollencount.html', pollen_count=100)


@app.route('/pollen/')
@app.route('/pollen/<name>')
def pollen():
    r1 = requests.get('http://localhost:5000/getPollenCountFromAPI')
    x = r1.json()
    # print(type(x))

    return render_template('pollencount.html', pollen_count=x[0]["pollen_count"])

@app.route('/date/')
def date():
    r2 = requests.get('http://localhost:5000/getPollenCountFromAPI')
    y = r2.json()
    return render_template('pollencount.html', pollen_count=y[0]["date"])


@app.route("/", methods=['GET'])
def allergy_alerts():

    r1 = requests.get('http://localhost:5000/getPollenCountFromAPI')
    return r1.content

if __name__ == "__main__" :app.run(host='127.0.0.1', port=8001)


