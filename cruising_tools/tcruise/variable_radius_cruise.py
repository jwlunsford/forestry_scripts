#!/usr/bin/env python
import pandas as pd
import numpy as np
import sys
from .yield_eqs.pmrc import pmrc_ucp_tons, pmrc_lcp_tons

'''This module calculates variable radius point sampling cruise data.
   Point data are input into a CSV file in the local directory and 
   calculations are done using NumPy and Pandas modules.  The default
   basal area factor is 10.

   Volume equations are currently set to use pmrc_ucp_tons, but this can be
   changed in the code below on line 54.
'''

class PointSample:
    
    def __init__(self, path):
        self.path = path
                
    
    def run(self):
        # get the baf from the user
        baf = int(input("What is the Basal Area Factor? > "))
        
        # run the calculations and display the results
        raw_df = self._gen_df(self.path)
        calc_df = self._calc_data(raw_df, baf)
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
    

    def _calc_data(self, raw_df, baf=10):
        # accepts a newly created dataframe from the csv data and
        # appends additional values to the dataframe
        try:
            # determine the number of unique plots
            plot_count = 0
            for n in raw_df.PLT.unique():
                plot_count += 1
                
            # create new data columns on the raw dataframe
            raw_df.insert(6, "BAT", np.power(raw_df.DBH, 2) * 0.00545415) #BArea
            raw_df.insert(7, "PAE", (baf/raw_df.BAT))  # Per Acre Expansion
            raw_df.insert(8, "TPA", raw_df.PAE/plot_count)  # Trees per Acre
            raw_df.insert(9, "VOL", pmrc_ucp_tons(raw_df.DBH, raw_df.THT)) # Volume/T
            raw_df.insert(10, "VPA", raw_df.VOL * raw_df.TPA) # Volume per Acre
            raw_df.insert(11, "BAPA", raw_df.BAT * raw_df.TPA) # Basal Area per Acre
               
            return raw_df
            
        except ValueError:       
            print("This will create a duplicated column in the raw dataframe."
                " If this is your intention, then allow_duplicates=True"
                " should be added to the DataFrame insert() method.")
            sys.exit(1)
        
        

    def _sum_data(self, df):
        # accepts a modified dataframe with appended calculations    
        try:
            # group by products and aggregate per acre values
            grp = df.groupby(["SPP", "PRD"]).sum()
            grp = grp[["VPA", "TPA", "BAPA"]]  # show only these columns
            return grp
        except:
            pass
            

if __name__ == '__main__':
    # create  a PointSample class, run the calculations and print results
    PointSample(sys.argv[1]).run()
    print("\n {} \n".format(output))
    
        