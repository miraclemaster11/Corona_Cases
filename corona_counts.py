# import libraries
import requests
from bs4 import BeautifulSoup
import time
import folium
from geopy.geocoders import ArcGIS

url = "https://www.worldometers.info/coronavirus/"
id = input("Enter the name of country:\t").lower()
print("\n\n")

nom = ArcGIS()
nom = nom.geocode(id)

coordinate = nom[-1]
mapped_object = folium.Map(location=coordinate, zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
if len(id.split()) > 1:
    id = ("-").join(id.split())

place = ""

if id:
    place = "/country/" + id + "/"

url = url + place
time.sleep(1)
r = requests.get(url)
doc = BeautifulSoup(r.text, "html.parser")

stats = [count.text for count in doc.select(".maincounter-number")]

# Cases Death Recovered
condition = ["Cases", "Deaths", "Recovered"]
i = 0
result = ""
for stat in stats:
    result += condition[i] + " : " + stat.split()[0] + "\n"
    i += 1

fg.add_child(folium.Marker(location=coordinate, popup=result, icon=folium.Icon(color="Green")))
mapped_object.add_child(fg)
mapped_object
#TESTING TESTING TESTING miraclemaster
