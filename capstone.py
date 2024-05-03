from flask import Flask, request, render_template
from predict import getModelPrediction

app = Flask(__name__)

@app.route("/predict")
def predict():
    isSouthernMetro = request.args.get('isSouthernMetro', "y").lower() == "y"
    rooms = int(request.args.get('rooms', 4))
    bathrooms = float(int(request.args.get('bathrooms', 2)))
    isHouse = request.args.get('isHouse', "y").lower() == "y"
    lat = float(request.args.get('lat', "-37.81"))
    lon = float(request.args.get('lon', "144.96"))

    price = getModelPrediction(isSouthernMetro, rooms, bathrooms, isHouse, lat, lon)

    return render_template("predict.html", isSouthernMetro=isSouthernMetro, rooms=rooms, bathrooms=bathrooms, isHouse=isHouse, lat=lat, lon=lon, price=price)
