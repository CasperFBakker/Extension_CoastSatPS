import os
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

class Waterheigth_Correction():


    def Extract_DateTime_FromImagery(self, folder_path):
        """
        Reads the start of the imagery name, that contains the
        date and the time, when the image was captured.

        Parameters:
            folder_path : Directory to the imagery files
        Returns:
            DateTimeFromFiles : list of all extracted date-time 
        """

        DateTimeFromFiles = []
        for filename in os.listdir(folder_path):
            if filename.endswith('.tif'):
                DateTimeFromFile = filename[:15]
                DateTimeFromFiles.append(DateTimeFromFile)

        DateTimeFromFiles = sorted(list(set(DateTimeFromFiles)))

        return DateTimeFromFiles

    def Reformat_DateTime2Unix(self, DateTimeFromFiles):
        """
        Reformat the Extracted date-time (yyyy_mm_dd hh:mm:ss)
        to unix timestamp (ms since 1970)

        Parameters:
            DateTimeFromFiles : list of all extracted date-time in format (yyyy_mm_dd hh:mm:ss)
        Returns:
            epochTime : list of all extracted date-time in epoch format
        """

        epochTime = []
        for i, value in enumerate(DateTimeFromFiles):
            date_object = datetime.datetime.strptime(value, "%Y%m%d_%H%M%S")
            timestamp = time.mktime(date_object.timetuple())
            milliseconds = int(timestamp * 1000)
            epochTime.append(milliseconds)

        return epochTime

    def FindClosest_WaterheightMeasurement(self, epochTime, MeasurementTime, MeasurementWH):
        """ 
        Find the closest measurement of the waterheigth to the 
        time the imagery was captured. 

        Parameters:
            epochTime :  list of all extracted date-time in epoch format
            MeasurementTime : array of the measurements times (epoch)
            MeasurementWH : array of the measurement waterheigths [m NAP]
        Returns:
            WH: list of all corresponding waterheigths [m NAP]
        """

        WH = []
        for i, value in enumerate(epochTime):
            differences = np.abs(MeasurementTime - value)
            index = np.where(differences == differences.min())[0][0]
            WH.append(MeasurementWH[index])

        return WH

    def Compute_WaterCor(self, folder_path, MeasurementData, slope=1/7.8):
        """
        Function that compute the correction for the waterheight
        from a .csv-file with time-evolution of waterlevel and 
        uses the input names of the satellite-imagery for the 
        date/time. 

        Parameters:
            folder_path : Directory to the imagery files
            MeasurementData : .csv-file with 1st column time [epoch] 2th column waterheight (m)
            slope : slope of the beach-face (default:1/13)
        returns:
            WH_Correction :  the cross-shore correction of the shoreline [m]
        """

        MeasurementTime = MeasurementData[:,0]
        MeasurementWH = MeasurementData[:,1]

        DateTimeFromFiles = self.Extract_DateTime_FromImagery(folder_path)
        epochTime = self.Reformat_DateTime2Unix(DateTimeFromFiles)
        WH = self.FindClosest_WaterheightMeasurement(epochTime, MeasurementTime, MeasurementWH)
        WH_Correction = []
        for index, value in enumerate(WH):
            Xcor = ((value - 0)/(slope))
            WH_Correction.append(Xcor)


        DateTimeFromFilesSeries = pd.Series(DateTimeFromFiles, name="Satellite Imagery date: "); 
        WH_CorrectionSeries = pd.Series(WH_Correction, name="Xcor [m]")

        df = pd.merge(DateTimeFromFilesSeries,WH_CorrectionSeries, right_index = True, left_index = True)
        fileName = 'Waterheigth_Cor_' + os.path.basename(os.path.dirname(folderPath)) + ".csv"
        df.to_csv(fileName, index=False)

        return WH_Correction

if __name__ == '__main__':
    MeasurementData = np.array(pd.read_csv('/home/casper/Documents/Aardwetenschappen/Marker_Wadden/Marker_Wadden_GH/New_script/Waterheight_Zuidstrand.csv'))
    folderPath = '/home/casper/Documents/Aardwetenschappen/Marker_Wadden/Marker_Wadden_GH/CoastSat_PlanetScope/user_inputs/Satellite_Imagery/MarkerWadden_1821_GeoRef/'
    ThisClass = Waterheigth_Correction()
    print(ThisClass.Compute_WaterCor(folderPath, MeasurementData))