#!/usr/bin/env python
import pandas as pd
import numpy as np
from scipy import stats
import sys
from .yield_eqs.yield_functions import pmrc_ucp_tons, pmrc_lcp_tons,
    gfc79_loblolly, gfc60_hard_hardwood

'''This module calculates variable radius point sampling cruise data.
   Point data are input into a CSV file in the local directory and
   calculations are done using NumPy and Pandas modules.  The default
   basal area factor is 10.

   Volume equations are currently set to use pmrc_ucp_tons, but this can be
   changed in the code below on line 93.

   *** This Version was changed to include a single PRD column instead of a
   SPP & PRD combination. ***
'''

class PointSample:

    def __init__(self, path):
        self.path = path
        self.dframes = {}
        self.plots = 0
        self.means = []
        self.stats = []


    def calculate(self):
        # get the baf from the user
        baf = int(input("What is the Basal Area Factor? > "))

        # run the calculations and display the results
        self._gen_df(self.path)
        self._calc_data(self.dframes["raw_df"], baf)
        self._sum_data(self.dframes["calc_df"])
        self._calc_stats(self.dframes["calc_df"])

        self._display()


    def _display(self):
        # display the means
        print("Stocking by Species and Product (per acre) .... \n")
        for row in self.means:
            print("STD: {0}, PRD: {1},  TPA: {2:6.2f},  BA: {3:5.2f},  TONS: {4:8.2f}".
                format(row[0], row[1], row[2], row[3], row[4]))

        # print new line
        print("\n")

        # display the stats
        print("Per acre Stats ....\n")
        for label, value in self.stats:
            print("{0:<18s}: {1:6.2f}".format(label, value))


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
            self.plots = plot_count

            # df references the raw_df, make a copy so it is left unchanged
            calc_df = df.copy()

            # create new data columns on the raw dataframe
            # BAT = basal area per tree
            # PAE = per acre expansion factor
            # TPA = trees per acre
            # VOL = volume per tree
            # VPA = volume per acre
            # BAPA = basal area per acre
            calc_df.insert(5, "BAT", np.power(calc_df.DBH, 2) * 0.00545415)
            calc_df.insert(6, "PAE", (baf/calc_df.BAT))
            calc_df.insert(7, "TPA", calc_df.PAE)
            calc_df.insert(8, "VOL", pmrc_ucp_tons(calc_df.DBH, calc_df.THT))
            calc_df.insert(9, "VPA", calc_df.VOL * calc_df.TPA)
            calc_df.insert(10, "BAPA", baf)

            # store the calc dataframe in self.dframes dict
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
            # have to divide these by plot count
            grp = out_df[["STD", "PRD", "TPA", "VPA","BAPA"]].groupby(
                ["STD", "PRD"]).sum()/self.plots

            # create a summary dict of values SPP, PRD, TPA, VPA, BAPA
            # for each species-product combination.
            grp_means = []  # will hold means in a tuple
            for index, row in grp.iterrows():
                grp_std = index[0]
                grp_prd = index[1]
                grp_tpa = row["TPA"]
                grp_ba = row["BAPA"]
                grp_vol = row["VPA"]
                grp_means.append(
                    (grp_std, grp_prd, grp_tpa, grp_ba, grp_vol))

            # store grp_means in the means attribute
            self.means = grp_means

            # store the dataframe in self.dframes dict
            self.dframes["out_df"] = grp

        except:
            pass


    def _calc_stats(self, df): # CHANGE CALS BY STAND

        # accepts a calc dataframe, groups by plot, and return a Dict of stats

        # df refrences calc_df, which we want to leave unchanged, make a copy
        dfs = df.copy()

        # group by plot
        grp = dfs.groupby(["PLT"]).sum()

        # insert a new column with squared VPA values
        grp.insert(9, "VPA2", np.power(grp.VPA, 2))

        # sum VPA (this is sumX)
        sumX = grp["VPA"].sum()

        # average VPA (this is meanX)
        meanX = grp["VPA"].mean()

        # count VPA (this is number of plots - n)
        plt_ct = grp["VPA"].count()

        # sum VPA2 (this is sumX2)
        sumX2 = grp["VPA2"].sum()

        # summary basal area per acre
        t_BA = grp["BAPA"].sum() / self.plots

        # summary trees per acre
        t_TPA = grp["TPA"].sum() / self.plots

        # STATS.....
        # calc STD, SX, SE%, CV%
        std = np.power((sumX2 - np.power(sumX, 2)/plt_ct) / (plt_ct - 1), 0.5)
        std_error = std / np.power(plt_ct, 0.5)
        cv_pct = (std / meanX) * 100

        # calculate sampling error.  Need degrees of freedom and critical t-value
        degf = plt_ct - 1
        t = stats.t.ppf(0.975, degf)

        smp_error = (std_error / meanX) * 100 * t

        ci_upper = meanX + std_error * t
        ci_lower = meanX - std_error * t

        # return values in a List of tuples
        stat_list = [("Trees/Acre", t_TPA), ("Basal Area/Acre", t_BA),
                     ("Mean Tons", meanX), ("Upper Tons", ci_upper),
                     ("Lower Tons", ci_lower), ("Std. Deviation", std),
                     ("Std. Error", std_error), ("CV%", cv_pct),
                     ("Sampling Error", smp_error)]

        self.stats = stat_list



if __name__ == '__main__':
    # create  a PointSample class, run the calculations and print results
    ps = PointSample(sys.argv[1])
    ps.run()
    ps.stats()


