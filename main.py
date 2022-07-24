import functions as func
import os

os.chdir("Pacmann/TUGAS/Advanced Data Manipulation/tugas_4")

cars_data = func.open_file("data/autos.csv")
cars_data = func.rename_column_name(cars_data, {"dateCreated": "ad_created",
    "dateCrawled": "date_crawled",
    "fuelType": "fuel_type",
    "lastSeen": "last_seen",
    "monthOfRegistration": "registration_month",
    "notRepairedDamage": "unrepaired_damage",
    "nrOfPictures": "num_of_pictures",
    "offerType": "offer_type",
    "postalCode": "postal_code",
    "powerPS": "power_ps",
    "vehicleType": "vehicle_type",
    "yearOfRegistration": "registration_year"})
cars_data = func.change_to_datetime(cars_data, ["ad_created", "date_crawled", "last_seen"])
cars_data = func.clean_odometer(cars_data)
cars_data = func.clean_price(cars_data)
cars_data = func.drop_columns(cars_data, ["seller", "offer_type", "model", "num_of_pictures", "name", "postal_code"])
cars_data = func.filter_based_on_price(cars_data, 500, 40000)
cars_data = func.impute_object(cars_data, ["vehicle_type", "gearbox", "fuel_type", "unrepaired_damage"])
cars_data = func.normalization(cars_data)
cars_data = func.one_hot_encoding(cars_data)
cars_data = func.reset_index(cars_data)