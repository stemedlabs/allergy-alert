from flask import Flask, request, jsonify
from data_client import get_pollen_data

# get pollen count

app = Flask(__name__)
app.run(host='127.0.0.1', port=5000)


#get pollen count
@app.route("/getPollenCountFromAPI", methods=['GET'])
def getPollenCount():
    pollen_data_from_data_client = get_pollen_data()
    return jsonify(pollen_data_from_data_client)




