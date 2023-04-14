import simplekml
import pandas as pd
from geopy.geocoders import Nominatim

print("CAUTION!!! Make sure your file is titled 'coordinates.csv\n")

# reads coordinates from your .csv file
df = pd.read_csv('coordinates.csv')

# up to three addresses recommended not required
print("Please input your subject's top three addresses below.\n")

address1 = input("Address 1: ")
address2 = input("\nAddress 2: ")
address3 = input("\nAddress 3: ")

# uses geopy to get the latitude and longitude coordinates for the addresses from user input
geolocator = Nominatim(user_agent="loadrr")
location1 = geolocator.geocode(address1)
location2 = geolocator.geocode(address2)
location3 = geolocator.geocode(address3)
new_coord1 = (location1.longitude, location1.latitude)
new_coord2 = (location2.longitude, location2.latitude)
new_coord3 = (location3.longitude, location3.latitude)

# saves coordinates in a kml file 
kml = simplekml.Kml()

# loops through each row in the csv file and adds a place marker in the kml file
for index, row in df.iterrows():
    # initiates a new place market in the kml file with the coordinates from .csv
    kml.newpoint(name=f"Coordinate {index+1}", coords=[(row['Longitude'], row['Latitude'])])

# adds new place markers to the kml file
new_point1 = kml.newpoint(name=f"{address1}", coords=[new_coord1])
new_point1.style.iconstyle.color = simplekml.Color.red  
new_point2 = kml.newpoint(name=f"{address2}", coords=[new_coord2])
new_point2.style.iconstyle.color = simplekml.Color.green  
new_point3 = kml.newpoint(name=f"{address3}", coords=[new_coord3])
new_point3.style.iconstyle.color = simplekml.Color.purple  

print("\nAddress 1 will be plotted as a red pin. \nAddress 2 will be plotted as a green pin. \nAddress 3 will be plotted as a purple pin\n")

kml.save('mapped_coordinates.kml')

print("Your new file is saved as 'mapped_coordinates.kml'")