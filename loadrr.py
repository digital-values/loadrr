#!/bin/bash
import simplekml
import pandas as pd

print("Make sure your file is titled 'coordinates.csv'")

df = pd.read_csv('coordinates.csv')

kml = simplekml.Kml()

#update kml file with user input of address long lat conversion
print("Please input subject's top locations in the following format: 'Street Address, City, State, Zip code'")

# Loop through each row in the CSV file and add a placemark to the KML file
for index, row in df.iterrows():
    # Add a placemark to the KML file for the coordinate
    kml.newpoint(name=f"Coordinate {index+1}", coords=[(row['Longitude'], row['Latitude'])])

# Save the KML file
kml.save('mapped_coordinates.kml')