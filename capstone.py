from flask import Flask, request, render_template

app = Flask(__name__)

# http://127.0.0.1:5000/predict?isSouthernMetro=y&rooms=3&bathrooms=2&isHouse=y&lat=-35&lon=135

def getModelPrediction(isSouthernMetro, rooms, bathrooms, isHouse, lat, lon):
    isUnit = not isHouse

    return 1.0


@app.route("/predict")
def predict():
    isSouthernMetro = request.args.get('isSouthernMetro', "y").lower() == "y"
    rooms = int(request.args.get('rooms', 4))
    bathrooms = float(int(request.args.get('bathrooms', 2)))
    isHouse = request.args.get('isHouse', "y").lower() == "y"
    lat = float(int(request.args.get('lat', "-37.81")))
    lon = float(int(request.args.get('lon', "144.96")))

    price = getModelPrediction(isSouthernMetro, rooms, bathrooms, isHouse, lat, lon)

    return render_template("predict.html", isSouthernMetro=isSouthernMetro, rooms=rooms, bathrooms=bathrooms, isHouse=isHouse, lat=lat, lon=lon, price=price)
