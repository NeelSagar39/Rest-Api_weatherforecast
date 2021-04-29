import json
from datetime import datetime

import googlemaps


def timed_job():
    gmaps = googlemaps.Client(key="AIzaSyB9cg4Hwx8RTcNsjQlrhUGS1KwX8pQfqYw")
    # Request directions
    now = datetime.now()
    time = {'time': str(now)}
    with open('routes.json') as json_file:
        routes = json.load(json_file)

    route_dict = {}
    for key in routes.keys():
        curr_route = routes[key]
        directions_result = gmaps.directions(curr_route['startpoint'], curr_route['endpoint'], mode="transit")
        duration = int(str(directions_result[0].get("legs")[0].get("duration").get('text')).split(' ')[0])
        temp = {key: duration}
        route_dict.update(temp)
    route_dict.update(time)
    print('Dictionary made now Writing to file ......')
    return route_dict
