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
    print(data)
    for x in data['waypoints']:
        print(x["name"],x["location"])
    return data['routes'][0]['geometry']

# Bounding box for the random coordinates (e.g., [min_lat, min_lon, max_lat, max_lon])
bbox = [42.9462998575584, -2.6750931575636256, 56.36975981291837, 29.317094165353677]

# Generate random start and end coordinates
start = random_coordinates(bbox)
end = random_coordinates(bbox)

# Get the route
route = get_route(start, end, vehicle='train')

# Print the route geometry
print(route)
