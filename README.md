# loadrr
This script was developed with law enforcement as the end user due to the fact that they are one of the handful of legal authorities allowed to subpoena telephone providers for cellphone pings. At best this script serves as a quick resource to provide users with a common operating picture from the tactical perspective of an investigation. Similar scripts, programs, and actual commercial software do in fact exist, however, the majority fail at two basic principles: speed and simplicity.

A local deputy sheriff investigating a crime will most likely never take the time to learn technical skills as typical law enforcement investigations have a dedicated timeline aligned with the prosecution team's goals. 'Loadrr' was developed to provide a quick and simple resource to plot latitude and longitude coordinates on a kml map (derived from subpoena returns) and prompt an upload to google earth to then enable the user to screenshot the results for additional analysis at a later date.

One of the most frustrating issues I personally dealt with during my tenure at DEA was receiving a subpoena return for cellphone pings from telephone provider, loading the results into semi-complex commercial software, and wait for an eternity to see the pixelated results. Then I would tinker with google earth, knowing all of this could be automated. 

*STEPS FOR USE:*

1A: DOES YOUR AGENCY ALLOW YOU TO RUN SCRIPTS? IF NO - GO 1B. IF YES - FOLLOW ADDITIONAL STEPS BELOW:
1B: IS THERE A DEDICATED CRIMINAL ANALYST IN YOUR AGENCY? IF NO - REQUEST CLOUD VERSION OF PROGRAM HERE LOADRRCLOUD@CYBERSALOON.IO. IF YES - HAVE THEM FOLLOW ADDITIONAL STEPS BELOW:

1. Ensure Python3 is installed
    Windows PowerShell Command: python --version

2. Create new folder 
    Add results of subpoena in .csv format. Colummn 1 will be "Latitude"; Colummn 2 will be "Longitude" 
    (also attached a template)

3. Download loadrr.py file in the same folder as your .csv with the coordinates
    ensure both files exist in the same folder

4. Run the script
    Windows Command Line Interface:
    Windows Powershell:

5. Open Google Earth in an incognito window of your browser of choice and load your newly made kml file 

6. Do not save the project, take a screenshot or manipulate the viewing range as needed.