#!/bin/bash
import simplekml
import pandas as pd

# Read in the CSV file of coordinates
df = pd.read_csv('coordinates.csv')

# Create a KML file to hold the placemarks
kml = simplekml.Kml()

#update kml file with user input of address long lat conversion

# Loop through each row in the CSV file and add a placemark to the KML file
for index, row in df.iterrows():
    # Add a placemark to the KML file for the coordinate
    kml.newpoint(name=f"Coordinate {index+1}", coords=[(row['Longitude'], row['Latitude'])])

# Save the KML file
kml.save('coordinates.kml')
