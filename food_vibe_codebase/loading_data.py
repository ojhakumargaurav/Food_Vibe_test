import pandas as pd
import os
from mongoengine import connect
from food_vibe_model.models import restaurant
import numpy as np
import json
properties_file_path = "food_vibe_codebase\\food_vibe_properties.json"


def read_properties():
    with open(properties_file_path) as f:
        app_config = json.load(f)
        if ("MONGODB_URL" in app_config.keys()):
            connect(host=app_config.get("MONGODB_URL", ""))


def load_data_from_csv():
    read_properties()
    directory = "food_vibe_codebase\\csv_data\\"
    restaurant_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                path = os.path.join(root, file)
                country_details = file.replace("Test-", "").replace(".csv", "")
                csv_file_read = pd.read_csv(path, encoding='ISO-8859-1')
                csv_file_read = csv_file_read.assign(
                    country_details=country_details)
                csv_file_read = csv_file_read.rename(
                    columns={"Cost for two": "Cost_for_two", "Open Now": "Timings", "ï»¿Name": "Title", "Tag": "Tags"})
                csv_file_read = csv_file_read.replace(np.nan, "", regex=True)
                restaurant_list.extend(csv_file_read.to_dict("records"))
    restaurant_list_objects = []
    for restaurant_temp in restaurant_list:
        restaurant_list_objects.append(restaurant(**restaurant_temp))

    inserted_objects = restaurant.objects.insert(restaurant_list_objects)
    return len(inserted_objects)
