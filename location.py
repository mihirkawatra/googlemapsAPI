# Flask App to get a post request with "origin" and "destination" and return the directions in simple text format
import requests
from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route('/direct', methods=['POST'])
def directions():
    api_key = ""
    mode = "walking"
    origin = request.json["origin"]
    origin = origin.replace(" ","+")
    destination = request.json["destination"]
    destination = destination.replace(" ", "+")
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + origin + "&destination=" + destination + "&mode=" + mode + "&key=" + api_key
    api_data = requests.get(url)
    output = api_data.json()
    try:
        steps=[]
        for item in output["routes"][0]["legs"][0]["steps"]:
            if ('maneuver' in item.keys()):
                steps.append("After " + item["distance"]["text"] + item["maneuver"])
            else:
                steps.append("Go straight for " + item["distance"]["text"])
        return jsonify(steps)
    except:
        print("Some Error Occured!")
        print(output)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
