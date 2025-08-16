import requests

def get_address(lat, lon, api_key):
    url = "http://api.positionstack.com/v1/reverse"
    params = {
        'access_key': api_key,
        'query': f"{lat},{lon}",
        'limit': 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    if 'data' in data and len(data['data']) > 0:
        return data['data'][0]['label']  # Full address
    else:
        return "No address found."

api_key = "d79ab744ca2d0fcd04dfd8e71ae0b6db"
lat = 6.6778
lon = 3.1654

address = get_address(lat, lon, api_key)
print("Full Address:", address)
