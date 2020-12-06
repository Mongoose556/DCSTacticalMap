import json
import folium
# import fastapi

filename = "airports_json.json"

with open(filename, 'r') as json_file:
    data = json.load(json_file)
    # data is now a dictionary
    airports = data

m = folium.Map(
location=[36.18069839477539, 37.22439956665039],
zoom_start=12,
tiles='Stamen Terrain')

# https://www.programiz.com/python-programming/nested-dictionary

for bases, info in airports.items(): # for keys and values
    '''
    dictLength = len(airports)
    print("Dict len =", dictLength)
    
    dictItems = airports.items()
    print("name: ", dictItems)
    
    dictValues = airports.values()
    print("\nvalues: ", dictValues)
    
    print(info[0]) # prints array 0 Aleppo
    print("\nLen of info: ", len(info))
    # print(type(airports))
    '''
    
    for x in range(len(info)): # loop for total items in info 0-6
        #print(info[x])
        base_data = {}
        base_data = info[x]
        print("\nKeys:", base_data.keys()) # Keys: dict_keys(['name', 'city', 'country', 'IATA', 'ICAO', 'lat', 'lon', 'timezone', 'side'])
        print("\nValues: ", base_data.values()) # Values:  dict_values(['Incirlik', 'Adana', 'Turkey', 'N/A', 'N/A', '37.001944', '35.425833', '2', 'NATO'])
        
        locName = base_data.get("name")
        #print("\nLoc Name: ",locName)
        locCity = base_data.get("city")
        #print("City: ", locCity)
        locLat = base_data.get("lat")
        locLon = base_data.get("lon")
        locIATA = base_data.get("IATA")
        tooltip = locName
        popup = [locName, locLat, locLon]
        
        # add markers
        folium.Marker([base_data.get("lat"), base_data.get("lon")], 
        popup=popup, 
        tooltip=base_data.get("city"), 
        icon=folium.Icon(color=base_data.get('side'), icon='plane')).add_to(m)

# create file        
m.save("map.html")