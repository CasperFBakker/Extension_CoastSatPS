from Classes.AdditionalFunctions import *
from Classes.WaterheigthCorrection import *
from CoastSat_PS import settings as Input_Settings

def main():
    """ 
        Function to run the main script and skip the 
        steps that are unneccesary for this method. 
        (This script runs till line 122, check if this 
         untill step 4)
    """

    with open('CoastSat_PS.py', 'r') as file:
        script_lines = file.readlines() 
    script_to_execute = ''.join(script_lines[:122]) # read script till line 122
    exec(script_to_execute)

if __name__ == '__main__':

    print('========================== Step 1 ===========================')
    print('Translating the UDM to the same extent as the georeferenced imagery:')
    FunctionsClass = AdditionalFunctions()
    FunctionsClass.Translate_udmMask(Input_Settings['downloads_folder'])

    print('========================== Step 2 ===========================')
    print('Running the main script of CoastSat.PlanetScope')
    main()

    print('========================== Step 3 ===========================')
    print('Storing the output shorelines as .csv-files: ')
    pkl_file = 'shoreline outputs/Local Coreg/NDWI/Peak Fraction/' + str(Input_Settings['site_name']) + '_NDWI_Peak Fraction_shorelines.pkl'
    data = os.path.join('outputs', str(Input_Settings['site_name']), pkl_file)
    Storage_location = os.path.join('Shoreline_Positions/', str(Input_Settings['site_name']))
    if os.path.exists(Storage_location):
        FunctionsClass.Store_Coordinates(data, Storage_location)
    else:
        os.mkdir(Storage_location)
        FunctionsClass.Store_Coordinates(data, Storage_location)

    print('========================== Step 4 ===========================')
    print('Computing the cross-shore water correction: ')
    MeasurementData = np.array(pd.read_csv('/home/casper/Documents/Aardwetenschappen/Marker_Wadden/Marker_Wadden_GH/New_script/Waterheight_Zuidstrand.csv'))
    folderPath = '/home/casper/Documents/Aardwetenschappen/Marker_Wadden/Marker_Wadden_GH/CoastSat_PlanetScope/user_inputs/Satellite_Imagery/MarkerWadden_1821_GeoRef/'

    CorretionClass = Waterheigth_Correction()
    CorretionClass.Compute_WaterCor(folderPath, MeasurementData)
