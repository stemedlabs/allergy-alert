from flask import Flask, request, jsonify
import requests
from api import getPollenCount

app = Flask(__name__)

# getPollenCount

@app.route("/", methods=['GET'])

def allergy_alerts():

    r1 = requests.get('http://localhost:5000/getPollenCountFromAPI')
    return r1.content

if __name__ == "__main__" :app.run(host='127.0.0.1', port=8001)