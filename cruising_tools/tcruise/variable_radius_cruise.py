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
        self.dframes = {}
                
    
    def run(self):
        # get the baf from the user
        baf = int(input("What is the Basal Area Factor? > "))
        
        # run the calculations and display the results
        self._gen_df(self.path)
        self._calc_data(self.dframes["raw_df"], baf)
        self._sum_data(self.dframes["calc_df"])
        
        # print the result
        print("Summary by Species/Product...")        
        print("{} \n".format(self.dframes["out_df"]))
        
        
                
    def stats(self):
        # calculate and return the stats, pass in the calc_df
        stat_dict = self._calc_stats(self.dframes["calc_df"])
        
        # loop over the dictionary and print the stats
        print("Stats....")
        for key, value in stat_dict.items():
            print("{0:<10s}: {1:6.2f}".format(key, value))
        print("\n")
        
              
    
    def _gen_df(self, path_to_csv):
        # open the csv file and create a dataframe object
        # append the dataframe to self.dframes
        try:
            df = pd.read_csv(path_to_csv)
            self.dframes["raw_df"] = df
        except IOError:
            print("Error occured during csv import.")
            sys.exit(1)
    

    def _calc_data(self, df, baf=10):
        # accepts a newly created dataframe from the csv data and
        # appends additional values to the dataframe
        try:
            # determine the number of unique plots
            plot_count = 0
            for n in df.PLT.unique():
                plot_count += 1
                
            # df references the raw_df, make a copy so it is left unchanged
            calc_df = df.copy()
                
            # create new data columns on the raw dataframe
            calc_df.insert(6, "BAT", np.power(calc_df.DBH, 2) * 0.00545415) #BArea
            calc_df.insert(7, "PAE", (baf/calc_df.BAT))  # Per Acre Expansion
            calc_df.insert(8, "TPA", calc_df.PAE/plot_count)  # Trees per Acre
            calc_df.insert(9, "VOL", pmrc_ucp_tons(calc_df.DBH, calc_df.THT)) # Volume/T
            calc_df.insert(10, "VPA", calc_df.VOL * calc_df.TPA) # Volume per Acre
            calc_df.insert(11, "BAPA", calc_df.BAT * calc_df.TPA) # Basal Area per Acre
               
            self.dframes["calc_df"] = calc_df
            
        except ValueError:       
            print("This will create a duplicated column in the raw dataframe."
                " If this is your intention, then allow_duplicates=True"
                " should be added to the DataFrame insert() method.")
            sys.exit(1)
        
        

    def _sum_data(self, df):
        # accepts a calc dataframe, groups by spp/product   
        try:
            # df refrences calc_df, which we want unchanged, so make a copy
            out_df = df.copy()
            
            # group by products and aggregate per acre values
            grp = out_df.groupby(["SPP", "PRD"]).sum()
            grp = grp[["VPA", "TPA", "BAPA"]]  # show only these columns
            
            self.dframes["out_df"] = grp
        except:
            pass
            
            
    def _calc_stats(self, df):
        # accepts a calc dataframe, groups by plot, and return a Dict of stats
        
        # critical t values
        critical_t = {3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365,
                      8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179,
                      13: 2.160, 14: 2.145, 15: 2.131, 16: 2.120, 17: 2.110,
                      18: 2.101, 19: 2.093, 20: 2.086, 21: 2.080, 22: 2.074,
                      23: 2.069, 24: 2.064, 25: 2.060, 26: 2.056, 27: 2.052,
                      28: 2.048, 29: 2.045, 30: 2.042}
                      
        # df refrences calc_df, which we want to leave unchanged, make a copy
        dfs = df.copy()
        
        # group by plot
        grp = dfs.groupby(["PLT"]).sum()
        
        # insert a new column with squared VPA values
        grp.insert(11, "VPA2", np.power(grp.VPA, 2))
        
        # sum VPA (this is sumX)
        sumX = grp["VPA"].sum()
        
        # average VPA (this is meanX)
        meanX = grp["VPA"].mean()
        
        # count VPA (this is number of plots - n)
        plt_ct = grp["VPA"].count()
        
        # sum VPA2 (this is sumX2)
        sumX2 = grp["VPA2"].sum()
        
        # calc STD, SX, SE%, CV%
        std = np.power((sumX2 - np.power(sumX, 2)/plt_ct) / (plt_ct - 1), 0.5)
        std_error = std / np.power(plt_ct, 0.5)
        cv_pct = (std / meanX) * 100
        
        # calculate sampling error.  Need degrees of freedom and critical t-value
        degf = plt_ct - 1
        if degf < 3:
            t = critical_t[3]
        elif degf > 30:
            t = critical_t[30]
        else:
            t = critical_t[degf]
            
        smp_error = (std_error / meanX) * 100 * t
        
        # return Dict
        stats = {"MEAN": meanX, "STD": std, "STD_ERR": std_error, "CV": cv_pct,
                     "SMP_ERR": smp_error}
        return stats
        
          

if __name__ == '__main__':
    # create  a PointSample class, run the calculations and print results
    ps = PointSample(sys.argv[1])
    ps.run()
    ps.stats()
    
    
        