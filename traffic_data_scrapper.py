import googlemaps
from datetime import datetime
import json
# from apscheduler.schedulers.blocking import BlockingScheduler

def timed_job():
    gmaps = googlemaps.Client(key="AIzaSyB9cg4Hwx8RTcNsjQlrhUGS1KwX8pQfqYw")
    # Request directions
    now = datetime.now()
    time = {'time': str(now)}
    with open('routes.json') as json_file:
        routes = json.load(json_file)

    route_dict = {}
    #print('Connection Made!! now making a dictionary')
    for key in routes.keys():
        curr_route = routes[key]
        #print(curr_route)
        #print(curr_route['startpoint'],curr_route['endpoint'])
        directions_result = gmaps.directions(curr_route['startpoint'],curr_route['endpoint'], mode="transit")
        duration =int(str(directions_result[0].get("legs")[0].get("duration").get('text')).split(' ')[0])
        temp = {key:duration}
        route_dict.update(temp)
    route_dict.update(time)
    print('Dictionary made now Writing to file ......')
    # with open('durations_dataset.json', 'a') as outfile:
    #     json.dump(route_dict, outfile)
    #     outfile.write(',\n')
    # print('Done!')
    ##print(route_dict)
    return route_dict

# scheduler = BlockingScheduler()
# scheduler.add_job(timed_job, 'interval', hours=1)
# scheduler.start()

# if __name__ == '__main__':
#     timed_job()