# Extension for CoastSat.PlanetScope
Author: Casper Bakker, Utrecht University & Rijkswaterstaat (06/2023)

# Description
This package serves as an extension to the original code of: [CoastSat.PlanetScope](https://github.com/ydoherty/CoastSat.PlanetScope). It is designed to be installed alongside the original code and add additional functionality. The purpose of using CoastSat.PlanetScope is to determine the shoreline position and export it for further analysis. In this extension, the shoreline is converted to an area, which makes it easier to utilize in the time-series evolution of an entire beach. The image below shows an example of the potential output that can be created by this workflow.

![alt text](https://github.com/CasperFBakker/Extension_CoastSatPS/blob/main/readme_files/Example_ResultArea.png)

An extensive guide on how to use this package has been provided [here](https://github.com/CasperFBakker/Extension_CoastSatPS/tree/main/readme_files/GuideForCSPS.pdf). Step 4 in this guide is the use of this python file, where the main file consist of 4 (sub)steps:

1. Translating the UDM to the same extent as the georeferenced imagery.
2. Running the main script of CoastSat.PlanetScope'
3. Storing the output shorelines as .csv-files.
4. Computing the cross-shore water correction.


# Installation
To use this package, follow the installation instructions for CoastSat.PlanetScope. Once the original code is installed, add this package to the script.


# Usage
### Step 1:
This code was specifically applied to a study of the Marker Wadden, Netherlands. Due to significant spatial errors between different imagery, georeferencing was necessary. Because the absence of usable ground control points, the imagery was manually referenced using the ArcGIS Pro move tool. For other studies, it is recommended to assess whether this step is required, since it is a time-consuming task. 
### Step 2:
This part runs the original code of CoastSat.PlanetScope up to step 3 (Manual error detection). Ensure that the necessary user inputs are placed in the correct folder and verify that any modified settings are correctly configured.
### Step 3:
The output shorelines are stored as .csv files to aid further analysis in Python and other GIS software.
### Step 4:
The cross-shore distance for water correction is computed for each imagery and saved in a .csv file. This requires two inputs: a time-series .csv file containing water height data and the beach slope. In this study, it is assumed that the beach slope used for correction remains constant alongshore and over time. If using this code for a different study site, it is important to update the beach slope in this function.

For the final step, the extracted shoreline can be exported to GIS software, where it can be converted from a line to a polygon to analyze the beach area. A notebook has been provided for use in ArcGIS Pro.

