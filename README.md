# loadrr
Accepts coordinates and automates cellphone triangulation

To use this program, replace YOUR_API_KEY with your OpenCelliD API key and make sure that you have a CSV file named coordinates.csv in the same directory as the Python script, with the latitude and longitude coordinates in separate columns labeled Latitude and Longitude, respectively.

This program uses the simplekml library to create the KML file for Google Earth and the pandas library to read in the CSV file of coordinates. It also uses the requests library to make HTTP requests to the OpenCelliD API to get cell tower information for each coordinate.

After running this program, you can open the generated coordinates.kml file in Google Earth to view the placemarks for each coordinate and the cell tower information in the description.

#!/usr/bin/
import simplekml
import pandas as pd
import requests

# Function to get cell tower information from OpenCelliD API
#def get_cell_tower_info(lat, lon):
#    url = f"https://eu1.unwiredlabs.com/v2/process.php?key=0402238ccdb6b3b87f0535b5f317178c&lat={lat}&lon={lon}&format=json"
 #   response = requests.get(url)
  #  if response.status_code == 200:
   #     data = response.json()
    #    if 'error' not in data:
     #       return data['cells']
    #return []

#userInput = userInput()
print("Please enter your CSV file in the following format: coordinates.csv")

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


# Loop through each row in the CSV file and add a placemark to the KML file
#for index, colm in df.iterrows():
    # Get the cell tower information for the coordinate
    #cell_towers = get_cell_tower_info(colm['Latitude'], colm['Longitude'])
    # Create a description for the placemark with the cell tower information
    #description = "<b>Cell Towers:</b><br>"
    #for tower in cell_towers:
     #   description += f"  <i>ID:</i> {tower['cid']}<br>  <i>MCC:</i> {tower['mcc']}<br>  <i>MNC:</i> {tower['mnc']}<br><br>"
    # Add a placemark to the KML file for the coordinate
    #kml.newpoint(name=f"Coordinate {index+1}", coords=[(colm['Longitude'], colm['Latitude'])], description=description)

# Save the KML file
kml.save('coordinates.kml')
