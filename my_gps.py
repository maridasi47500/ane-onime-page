import random
import requests

# Function to generate random coordinates within a given bounding box
def random_coordinates(bbox):
    lat = random.uniform(bbox[0], bbox[2])
    lon = random.uniform(bbox[1], bbox[3])
    return lat, lon

# Function to get a route from OpenStreetMap
def get_route(start, end, vehicle='foot'):
    url = 'http://router.project-osrm.org/route/v1/{}/{},{};{},{}?steps=true&geometries=polyline&overview=full&annotations=true'.format(
        vehicle, start[1], start[0], end[1], end[0])
    response = requests.get(url)
    data = response.json()
    #print(data)
    print("DATA")
    for x in data:
        print(x)
    print(data["code"][0][0])
    print("DATA CODE")
    for x in data["code"][0][0]:
        print(x)
    print("DATA ROUTES")

    for x in data["routes"][0]:
        print(x)
    for x in data["routes"][0]:
        print(x)

    for x in data["routes"]:
        for y in x["legs"]:
            print("LEGS")
            for z in y:
                print("Z",z)
            print("distance",y["distance"])
            print("duration",y["duration"])
            print("summary",y["summary"])
            print("STEPS")
            step=0
            for z in y["steps"]:
                step+=1
                print("######step : "+str(step)+"#######")
                print("name : "+z["name"])
                print("rouler à  : "+z["driving_side"])
                #print("manoeuvre  : ")


                #print("bearing after : ",z["maneuver"]["bearing_after"])
                #print("bearing before ",z["maneuver"]["bearing_before"])
                print("location ",z["maneuver"]["location"])
                try:
                    print("modifier",z["maneuver"]["modifier"])
                except:
                    print("")
                print("type ",z["maneuver"]["type"])
                #print("intersections  : ")
                #for a in z["intersections"]:
                #    print("A",a)
                #for a in z:
                #    print("A",a)
        print("LEGS")
    for x in data['waypoints']:
        print(x["name"],x["location"])
    return data['routes'][0]['geometry']

# Bounding box for the random coordinates (e.g., [min_lat, min_lon, max_lat, max_lon])
bbox = [45.92675064614011, 5.081708599776381, 52.67509283688802, 28.19694284682927]

# Generate random start and end coordinates
start = random_coordinates(bbox)
end = random_coordinates(bbox)

# Get the route
route = get_route(start, end, vehicle='train')

# Print the route geometry
#print(route)
