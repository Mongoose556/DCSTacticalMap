"""
    GOAL: DCS map

    TODO: 

    Capture data from tacview or export stream (SQL)
    Query SQL
    Put data on map
    start small - list all the bases in play for sides, then all the recon targets
    later, add all blue aircraft and BRAA

"""

import folium               # mapping
from flask import Flask     # server
import geopy                # geolocation
import json                 # Jason Vorhees
import logging              # Canadians
from pathlib import Path    #  
# https://pypi.org/project/geopy/

logging.basicConfig(filename="tacMap.log", level=logging.INFO, format='%(levelname)s:%(message)s')

app = Flask(__name__)

# read the file

# recursive function listing all dictionary data
def get_all_values(nested_dictionary):
    for keys, value in nested_dictionary.items():
        if type(value) is dict:
            get_all_values(value)
        else:
            print(keys, ":", value)

#get_all_values(airports)

map_centre = [36.2021, 37.1343] #Alleppo

@app.route('/')
def index():
    # centre coords
    

    # "keys: value" is item?

    # create map object
    tacMap = folium.Map(
        location = map_centre,
        zoom_start = 9,
        tiles = 'Stamen Terrain', width='75%'
    )

    filename = "data/airports_json.json"

    if not Path(filename).is_file():
        raise ValueError(f"Could not find file! {filename}")

    with open(filename, 'r') as json_file:
        data = json.load(json_file)
        # data is now a dictionary
        airports = data

    locLatitude = ""
    locLongitude = ""
    locName = ""

    for values in airports:
    
#"bases":[
#       {
#          "name":"Aleppo Intl",
#          "city":"Aleppo",
#          "country":"Syria",
#          "IATA":"ALP",
#          "ICAO":"OSAP",
#          "lat":"36.18069839477539",
#          "lon":"37.22439956665039",
#          "timezone":"2",
#         "side": ""
#       },

    # "keys(reference): value(data)" is item
    # data["London"]["latitude"]

        tooltip = ""
        #get names
        names = values
        #get position
        locLatitude = airports(["lat"])
        locLongitude = airports(["long"])
        #get colour
        side = airports["side"]

        # add markers to map
        folium.Marker(position=[locLatitude, locLongitude],
        popup=f'<i>{names}</i>', 
        tooltip=tooltip, 
        icon=folium.Icon(color=side, icon='plane')).add_to(tacMap)

        tacMap.save('templates/map.html') # create html map

        return tacMap._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)