import requests

API_KEY = "W5MAUZY0DBgjcECm4mSkWoopwECwgjB0"

lat = 51.2194
lon = 4.4025

url = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"
params = {
    "point": f"{lat},{lon}",
    "key": API_KEY
}

resp = requests.get(url)

print(resp.json())