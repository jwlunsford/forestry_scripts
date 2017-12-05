#!/usr/bin/env python
import csv
import sys
import math

def num_plots():
    ''' This module calculates the number of plots required (by stratum) for a
        timber cruise using the optimum allocation method.

        This module requires 'sample.csv' to be present in the current working
        directory.  Use this file to add the input data.
        NOTICE:  The structure of the file should not be changed.

        Inputs from the sample.csv file (as comma seperated values)
            Col 1 = strata number
            Col 2 = strata description
            Col 3 = estimated volume/acre
            Col 4 = acres in strata
            Col 5 = estimated CV for strata

        Output:  Printed calculations for number of plots by stratum.
    '''

    # initialize variables to hold data during run
    strata_vol = []       # holds a list of stratum total volume cals (vol/ac * ac)
    strata_pct_vol = []   # holds a list of stratum percentage volume calcs
    strata_cv = []        # hold a modified list of the stratum cv values
    strata_cv_frac = []   # holds a list of CV fractions
    plots_by_strata = []  # will hold the final list of plots by strata
    sum_vol = 0           # running total of the strata volumes
    sum_acres = 0         # running total of the strata acres
    weighted_cv = 0       # running total of cv fractions
    t = 2                 # standard errors

    # user input
    sampling_error = input("Enter desired Sampling Error (i.e.; 10 for 10%) ")
    samp_err = int(sampling_error)


    try:
        file = open('data.csv')
        reader = csv.reader(file)

        # loop through strata building a sum of acres and vol
        for strata in reader:
            if reader.line_num == 1:
                continue    # skip the first row (headers)
            est_vol = float(strata[2]) * float(strata[3])
            strata_vol.append([strata[0], est_vol])
            strata_cv.append([strata[0], strata[4]])
            sum_vol += est_vol
            sum_acres += int(strata[3])
        
        # loop through the strata_vol list
        for strata in strata_vol:
            cur_pct = round(strata[1]/sum_vol, 2)
            strata_pct_vol.append([strata[0], cur_pct])
    
        zipped = zip(strata_pct_vol, strata_cv)

        for x in zipped:
            cv = x[0][1] * int(x[1][1])
            strata_cv_frac.append([x[0][0], cv])
            weighted_cv += cv
    
        tot_plots = round((math.pow(t, 2) * math.pow(weighted_cv, 2)) / 
                           math.pow(samp_err, 2), 0)
        
        # final loop through the cv fraction list          
        for strata in strata_cv_frac:
            strata_plots = round((strata[1] * (tot_plots / weighted_cv)), 0)
            plots_by_strata.append([strata[0], strata_plots])                
                

        # printouts
        print("\n")
        print("OUTPUT:")
        print("- " * 20)
        print("Total volume = {}".format(sum_vol))
        print("Total acres = {}".format(sum_acres))
        print("Weighted CV% = {}".format(weighted_cv))
        print("Total plots required (N) = {}".format(tot_plots))
        print("Plots by strata ...")
        for strata in plots_by_strata:
            print("  Strata {}: n={}".format(strata[0], strata[1]))
        print("\n")

        # the following are only needed for debugging...
        # print(strata_vol)
        # print(strata_pct_vol)
        # print(strata_cv_frac)

    except (FileNotFoundError, IOError):
        print("The file sample.csv could not be opened."
            "Please make sure it is in the working directory.")
        sys.exit()       
    else:
        file.close()

if __name__ == '__main__':
    num_plots()