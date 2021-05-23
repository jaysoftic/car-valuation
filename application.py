from flask import Flask, render_template, request
import json
import util
import datetime
application = Flask(__name__)
with open("artifacts/image_urls.json", "r") as f:
    images_urls = json.load(f)

util.load_artifacts()
car_name = util.get_car_name()
current_year = datetime.date.today().year
@application.route("/")
def home():
    return render_template("home.html", car_name = car_name, current_year = current_year)

@application.route("/gettingImages", methods=["POST"])
def gettingImages():
    selectedCar = request.form["selectedCar"]
    return {"currentImage": images_urls[selectedCar]}

@application.route("/gettingPrice", methods=["POST"])
def gettingPrice():
    car = request.form["car"]
    year = request.form["year"]
    kmDriven = request.form["kmDriven"]
    fuel = request.form["fuel"]
    mileage = request.form["mileage"]
    transmission = request.form["transmission"]
    engine = request.form["engine"]
    sellerType = request.form["sellerType"]
    owner = request.form["owner"]

    return util.get_car_price(car, year, kmDriven, fuel, sellerType, owner, mileage, engine, transmission)

# here is route of 404 means page not found error
@application.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    application.run()
