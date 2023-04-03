# loadrr
Accepts coordinates and automates cellphone triangulation

To use this program, replace YOUR_API_KEY with your OpenCelliD API key and make sure that you have a CSV file named coordinates.csv in the same directory as the Python script, with the latitude and longitude coordinates in separate columns labeled Latitude and Longitude, respectively.

This program uses the simplekml library to create the KML file for Google Earth and the pandas library to read in the CSV file of coordinates. It also uses the requests library to make HTTP requests to the OpenCelliD API to get cell tower information for each coordinate.

After running this program, you can open the generated coordinates.kml file in Google Earth to view the placemarks for each coordinate and the cell tower information in the description.