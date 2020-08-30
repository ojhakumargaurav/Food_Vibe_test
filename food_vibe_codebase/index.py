from bottle import route, run, response, request
import bottle
from loading_data import load_data_from_csv, read_properties
from food_vibe_model.models import restaurant
import json
import logging


class EnableCors(object):
    name = 'enable_cors'
    api = 2

    def apply(self, fn, context):
        def _enable_cors(*args, **kwargs):
            # set CORS headers
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
            response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

            if bottle.request.method != 'OPTIONS':
                # actual request; reply with the actual response
                return fn(*args, **kwargs)

        return _enable_cors


app = bottle.app()


@route("/testing")
def test():
    return "Hello World"


@route("/load-data")
def load_data():
    no_of_inserted = load_data_from_csv()
    return {"inserted_objects": no_of_inserted, "status": "sucess"}


@route("/list-restaurant/<page_no:int>/<no_of_records:int>")
def list_restaurant(page_no=0, no_of_records=320):
    list_restaurant = restaurant.load_page(page_no, no_of_records)
    list_restaurant = list(map(map_restaurant, list_restaurant))
    return {"restaurant_list": list_restaurant}


@route("/list-restaurant-search", method=["POST", "OPTIONS"])
def list_searched_restaurant():
    requested_data = request.json

    list_restaurant = restaurant.load_search_restaurant(
        requested_data["search_string"], requested_data["page_no"])
    list_restaurant = list(map(map_restaurant, list_restaurant))
    return {"restaurant_list": list_restaurant}


def map_restaurant(restaurant_obj):
    restaurant_obj = restaurant_obj.to_mongo().to_dict()
    restaurant_obj["_id"] = str(restaurant_obj["_id"])
    return restaurant_obj


read_properties()
app.install(EnableCors())
app.run()
