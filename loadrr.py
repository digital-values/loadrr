import simplekml
import pandas as pd
from geopy.geocoders import Nominatim

print("CAUTION!!! Make sure your file is titled 'coordinates.csv\n")

df = pd.read_csv('coordinates.csv')

#update kml file with user input of address long lat conversion
print("Please input your subject's top three addresses below.\n")

address1 = input("Address 1: ")
address2 = input("\nAddress 2: ")
address3 = input("\nAddress 3: ")

# Use geopy to get the latitude and longitude coordinates for the address
geolocator = Nominatim(user_agent="loadrr")
location1 = geolocator.geocode(address1)
location2 = geolocator.geocode(address2)
location3 = geolocator.geocode(address3)
new_coord1 = (location1.longitude, location1.latitude)
new_coord2 = (location2.longitude, location2.latitude)
new_coord3 = (location3.longitude, location3.latitude)

kml = simplekml.Kml()

# Loop through each row in the CSV file and add a placemark to the KML file
for index, row in df.iterrows():
    # Add a placemark to the KML file for the coordinate
    kml.newpoint(name=f"Coordinate {index+1}", coords=[(row['Longitude'], row['Latitude'])])

# Add a new placemark to the KML file for the new coordinate
new_point1 = kml.newpoint(name=f"{address1}", coords=[new_coord1])
new_point1.style.iconstyle.color = simplekml.Color.red  # Change the color of the first point
new_point2 = kml.newpoint(name=f"{address2}", coords=[new_coord2])
new_point2.style.iconstyle.color = simplekml.Color.green  # Change the color of the second point
new_point3 = kml.newpoint(name=f"{address3}", coords=[new_coord3])
new_point3.style.iconstyle.color = simplekml.Color.blue  # Change the color of the third point

# Save the KML file 
kml.save('mapped_coordinates.kml')