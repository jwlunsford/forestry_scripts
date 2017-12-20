#!/usr/bin/env python
import pandas as pd
import numpy as np
import sys
from pmrc import pmrc_ucp_tons

'''This module does a simple point sample workup.  Plot data are read from a
   CSV file and calculations are done using a Pandas DataFrame object.   
'''

class PointSample:
    
    def __init__(self, path):
        self.path = path
                
    
    def run(self):
        # run the calculations and display the results
        raw_df = self._gen_df(self.path)
        calc_df = self._calc_data(raw_df)
        output = self._sum_data(calc_df)
        return output        
        
    
    def _gen_df(self, path_to_csv):
        # open the csv file and create a dataframe object
        try:
            df = pd.read_csv(path_to_csv)
            return df
        except IOError:
            print("Error occured during csv import.")
            sys.exit(1)
    

    def _calc_data(self, raw_df):
        # accepts a newly created dataframe from the csv data and
        # appends additional values to the dataframe
        try:
            # create new data columns on the raw dataframe
            raw_df.insert(6, "BAT", np.power(raw_df.DBH, 2) * 0.00545415) #BArea
            raw_df.insert(7, "PAE", (10/raw_df.BAT))  # Per Acre Expansion
            raw_df.insert(8, "TPA", raw_df.PAE/4)  # Trees per Acre
            raw_df.insert(9, "VOL", pmrc_ucp_tons(raw_df.DBH, raw_df.THT)) # Volume/T
            raw_df.insert(10, "VPA", raw_df.VOL * raw_df.TPA) # Volume per Acre
            raw_df.insert(11, "BAPA", raw_df.BAT * raw_df.TPA) # Basal Area per Acre
               
            return raw_df
            
        except ValueError:       
            print("This will create a duplicated column in the raw dataframe."
                " If this is your intention, then allow_duplicates=True"
                " should be added to the DataFrame insert() method.")
            sys.exit(1)
        except:
            # syst.exc_info returns the tuple (type, value, traceback)
            print("Unexpected error in calc_data():", sys.exc_info()[0])
            sys.exit(1)
        

    def _sum_data(self, df):
        # accepts a modified dataframe with appended calculations    
        try:
            # group by products and aggregate per acre values
            grp = df.groupby(["SPP", "PRD"]).sum()
            grp = grp[["VPA", "TPA", "BAPA"]]  # show only these columns
            return grp
        except:
            # sys.exc_info returns the tuple (type, value, traceback)
            print("Unexpected error in sum_data():", sys.exc_info()[0]) 
            sys.exit(1)
            

if __name__ == '__main__':
    # create  a PointSample class, run the calculations and print results
    output = PointSample(sys.argv[1]).run()
    print("\n {} \n".format(output))
    
        