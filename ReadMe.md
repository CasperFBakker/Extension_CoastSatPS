# Extension for CoastSat.PlanetScope
Casper Bakker, Utrecht University & Rijkswaterstaat (06/2023)

# Description
This package has been created to be used as an extension to the original code of [CoastSat.PlanetScope](https://github.com/ydoherty/CoastSat.PlanetScope).
The idea behind this package is to install the original code of CoastSat.PlanetScope and to add this code to that script. 

An extensive guide on how to use this package has been added [here](https://github.com/CasperFBakker/Extension_CoastSatPS/tree/main/readme_files/GuideForCSPS.pdf).
This guide is based on the workflow shown below.
![alt text](https://github.com/CasperFBakker/Extension_CoastSatPS/blob/main/Example_ResultArea.png)


The main file runs 4 steps:
1. Translating the UDM to the same extent as the georeferenced imagery.
2. Running the main script of CoastSat.PlanetScope'
3. Storing the output shorelines as .csv-files.
4. Computing the cross-shore water correction.
# Installation



# Usage
### Step 1:
This code has been applied for a study of the Marker Wadden, Netherlands. This area is relatively small and the spatial errors between different imagery was too large to use uncorrected. So, the first step is to georeference all imagery. Because of the lack of the presence of useable ground control points at the Marker Wadden, the imagery are referenced by hand using the ArcGIS Pro move tool. For different studies it might be usefull to check if this step is necessary, since it is a time-consuming task. 
### Step 2:
The part runs the original code of CoastSat.PlanetScope, until step 3 (Manual error detection). It is important to have added the user_inputs in the correct folder and the check if the changed settings are corrected. 
### Step 3:
Now the output shorelines are stored as .csv-files to make it easier to work with for further analysis in python and to work further in GIS-software.
### Step 4:
The cross-shore distance for the water correction is computed for each imagery and stored in a .csv-file. For this there are two things needed. The first one is a .csv-file with a time-series of the waterheigth. And second thing is the beach slope. In this study it is assumed that the slope, used for the correction, is the same alongshore and through time. If this code will be used for a different study-site it is important to change the beach slope in this function. 

For the last part, the extracted shoreline is exported to GIS-software. Where it is changed from a line to a polygon to study the beach area. A notebook has been added that can be used in ArcGIS-Pro. 

