settings = {
    
    ### General Settings ###
    # Site name (for output folder and files) 
    'site_name': 'ZuidStrand_20212023_temp',
    # Maximum image cloud cover percentage threshold
    'cloud_threshold': 10, # Default 10
    # Minimum image AOI cover percentage threshold
    'extent_thresh': 25, # Default 80
    # Desired output shoreline epsg
    'output_epsg': '28992',


    ### Reference files (in "...CoastSat.PlanetScope/user_inputs/") ###
    # Area of interest file (save as .kml file from geojson.io website)
    'aoi_kml': 'Zuidstrand.kml',
    # Transects in geojson file (ensure same epsg as output_epsg)
    'transects': False, #'Zuidstrand_Transects.geojson', # False
        # If False boolean given, popup window will allow for manual drawing of transects
    # Tide csv file in MSL and UTC 
    'tide_data': 'STB_FL66_Waterhoogte.csv',
    # Local folder planet imagery downloads location (provide full folder path)
    'downloads_folder': '/home/casper/Documents/Aardwetenschappen/Marker_Wadden/Marker_Wadden_GH/CoastSat_PlanetScope/user_inputs/Satellite_Imagery/ZuidStrand_20212023/PSScene/',


    ### Processing settings ###
    # Machine learning classifier filename (in "...CoastSat.PlanetScope/classifier/models")
        # A new classifier may be re-trained after step 1.3. Refer "...CoastSat.PlanetScope/classifier/train_new_classifier.py" for instructions. 
    'classifier': 'ZS_All_tresh50_900000_NARRA_9639.pkl',
    # Image co-registration choice ['Coreg Off', 'Local Coreg', 'Global Coreg']
    'im_coreg': 'Local Coreg', # refer https://pypi.org/project/arosics/ for details on Local vs Global coreg. Local recommended but slower. 


    ### Advanced settings ###
    # Buffer size around masked cloud pixels [in metres]
    'cloud_buffer': 9, # Default 9 (3 pixels)  
    # Max distance from reference shoreline for valid shoreline [in metres]
    'max_dist_ref': 75, # Default 75
    # Minimum area (m^2) for an object to be labelled as a beach
    'min_beach_area': 20*2000, # Default 22500
    # Minimum length for identified contour line to be saved as a shoreline [in metres]
    'min_length_sl': 2500, # Default 500 
    # GDAL location setting (Update path to match GDAL path. Update 'coastsat_ps' to chosen environment name. Example provided is for mac)
    'GDAL_location': '/home/casper/anaconda3/envs/wlmw/bin/',
        # for Windows - Update 'anaconda2' to 'anaconda3' depending on installation version.
        # 'GDAL_location': r'C:\ProgramData\Anaconda3\envs\coastsat_ps\Library\bin',

    #### Additional advanced Settings can be found in "...CoastSat.PlanetScope/coastsat_ps/data_import.py"

    }

