# read tacview file data in to a database
# read database
# parse data to map
# display map

# to run locally: uvicorn main:app --reload

import folium               # mapping
from fastapi import FastAPI     # server
# import geopy                # geolocation
import json                 # Jason Vorhees
import logging              # Canadians
from pathlib import Path    # 

from typing import Optional

app = FastAPI()

logging.basicConfig(filename="tacMap.log", level=logging.INFO, format='%(levelname)s:%(message)s')

path = "data"
filename = "data/airports_json.json"

with open(filename, 'r') as json_file:
    data = json.load(json_file)
    # data is now a dictionary
    airports = data

def create_map():
    
    # aleppo
    m = folium.Map(
    location=[36.18069839477539, 37.22439956665039],
    zoom_start=12,
    tiles='Stamen Terrain')
    
    return m


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}