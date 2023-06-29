import os
import sys
from tqdm import tqdm
import time
from osgeo import gdal
import rasterio

class Additional_Functions():

    def Translate_udmMask(path_of_dir, udm_path=None):
        """ 
            Function to copy the translated tiff 
            to traslate to the udm 

            Parameters:  
                path_of_dir: Directory where the Georeferenced files are
                udm_path: Directory where the udms files will be stored 
                        (default=same as georef files)
                
        """ 
        if udm_path is None: 
            udm_path = path_of_dir

        for files in tqdm(sorted(os.listdir(path_of_dir)), bar_format=' {percentage:3.0f}%|{bar}|'):
            if files.endswith('.tif'): #loop through georef images --> to get new extent 
                dataset = rasterio.open(os.path.join(path_of_dir, files))
                minX, maxY, maxX, minY = dataset.bounds
                new_Extent = [minX, minY, maxX, maxY]   
        
        
                for udm_files in sorted(os.listdir(udm_path)):
                    if udm_files.startswith(files[0:8]) and udm_files.endswith('.tif'): 
                        #loop through udm images --> to get new extent 
                        udm_inp = os.path.join(udm_path, udm_files)
                        udm_out = os.path.join(udm_path, 'new', udm_files)
                        gdal.Translate(udm_out, udm_inp, outputBounds = new_Extent)
            time.sleep(0.01)

        return



    def Store_Coordinates(data, path_of_dir):
        """ 
            Function to export the shorelines (from dictonary format)
            to .csv-files to work with it in ArcGIS Pro

            Parameters:  
                data: .pkl-file stored in the outputs from the CoastSat_PS.py script
                path_of_dir: location to store the .csv-files
                
        """ 

        SL = data["shorelines"]
        for i, value in tqdm(enumerate(SL), bar_format=' {percentage:3.0f}%|{bar}|'):
            date = data["date"]; time = data["time"]; 
            time = time[i]
            time = time[0:2] + time[3:5] + time[6:] 
            file_date = "SLPos_" + date[i] + '_' + time + ".csv"
            coords = SL[i]
            xlst = []; ylst = []
            for j, value in enumerate(coords):
                x = coords[j,0]; y = coords[j,1]
                xlst.append(x); ylst.append(y)
            
                x = pd.Series(xlst, name="x"); y = pd.Series(ylst, name="y")

                if not os.path.exists(path_of_dir):
                    os.makedirs(path_of_dir)

                df = pd.merge(x,y, right_index = True, left_index = True)
                df.to_csv(path_of_dir + file_date, index=False)
        time.sleep(0.01)

        return