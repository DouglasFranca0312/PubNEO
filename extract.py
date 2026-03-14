import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

all_neos = []

url = "https://api.nasa.gov/neo/rest/v1/neo/browse"

params = {
    "api_key": API_KEY,
    "page": 0
}

response = requests.get(url, params=params)
data = response.json()

total_pages = data["page"]["total_pages"]

all_neos.extend(data["near_earth_objects"])

for page in range(1, total_pages):

    params = {
        "api_key": API_KEY,
        "page": page
    }

    response = requests.get(url, params=params)
    data = response.json()

    all_neos.extend(data["near_earth_objects"])

with open("all_neos.json", "w") as f:
    json.dump(all_neos, f, indent=2)
