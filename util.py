import pandas as pd
import pickle

global car_name_encoded
global fuel_encoded
global seller_type_encoded
global model
def load_artifacts():
    global car_name_encoded
    global fuel_encoded
    global seller_type_encoded
    global model
    car_name_encoded = pd.read_csv("artifacts/car_name_encoded.csv")
    fuel_encoded = pd.read_csv("artifacts/fuel_encoded.csv")
    seller_type_encoded = pd.read_csv("artifacts/seller_type.csv")
    with open("artifacts/car_price_model.pickle", "rb") as f:
        model = pickle.load(f)

def get_car_name():
    car_name = car_name_encoded.name.sort_values().to_list()
    return car_name

def get_car_price(car, year, kmDriven, fuel, sellerType, owner, mileage, engine, transmission):
    try:
        car_encoded = car_name_encoded[car_name_encoded.name == car].index[0]
        fuel = fuel_encoded[fuel_encoded.fuel == fuel].index[0]
        sellerType = seller_type_encoded[seller_type_encoded.seller_type == sellerType].index[0]
        transmission = 1 if transmission == "Manual" else 0

        X_test = [[car_encoded, year, kmDriven, fuel, sellerType, owner, mileage, engine, transmission]]

        result = model.predict(X_test)[0]
        return "Predicted Price of " + car + " is <b>" + str(result) + "</b>"
    except:
        return "Something is wrong refresh the page and fill input properly!!"