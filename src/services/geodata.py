import requests
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path("./.env"))
def geo_data():
    response = requests.get("https://api.geoapify.com/v1/ipinfo?&apiKey=%s" % (os.getenv("GEO_API_KEY")))
    if response.status_code == 200:
        r = response.json()
        return [r['location'].get('latitude'), r['location'].get('longitude')]
    return None 
