# Extension for CoastSat.PlanetScope
Casper Bakker, Utrecht University & Rijkswaterstaat (06/2023)

# Description
This package has been created to be used as an extension to the original code of [CoastSat.PlanetScope](https://github.com/ydoherty/CoastSat.PlanetScope).
The idea behind this package is to install the original code of CoastSat.PlanetScope and to add this code to that script. 

An extensive guide on how to use this package has been added [here](https://github.com/CasperFBakker/Extension_CoastSatPS/tree/main/readme_files/GuideForCSPS.pdf).
This guide is based on the workflow shown below.
![alt text](https://github.com/CasperFBakker/Extension_CoastSatPS/blob/main/readme_files/WorkFlow.png)




This code has been applied for a study of the Marker Wadden, Netherlands. This area is relatively small and the spatial errors between different imagery was too large to use uncorrected. So, the first step is to georeference all imagery. Because of the lack of the presence of useable ground control points at the Marker Wadden, the imagery are referenced by hand using the ArcGIS Pro move tool. For different studies it might be usefull to check if this step is necessary, since it is a time-consuming task. 

When all files and user_inputs are changed

The main file runs 4 steps:
1. Translating the UDM to the same extent as the georeferenced imagery.
2. Running the main script of CoastSat.PlanetScope'
3. Storing the output shorelines as .csv-files.
4. Computing the cross-shore water correction.
