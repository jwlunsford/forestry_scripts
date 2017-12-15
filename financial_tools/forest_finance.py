#!usr/bin/env python

import pandas as pd
import numpy as np


def calc_lev(rate=0.04, rotation=30):
    '''This function will read cost/revenue data from a CSV file and 
    calculate the Land Expectation Value (LEV) - present value of 
    perpetual forest rotations.  The associated CSV file should be
    located in the same directory where the script is executed.
    '''
    discount_rate = 1 + rate
    
    dtable = pd.read_csv('lev_data.csv')  # read the csv into a Pandas dataframe
    
    # get the annual cost/revenue series data, denoted by FREQ = 0
    s_annual = dtable.loc[lambda dtable: dtable.FREQ == 0, :]
    
    annual_netrev = np.sum(s_annual['AMT']) / rate
    
    # get the intermediate cost/revenue series data, denoted by FREQ = 1
    s_interm = dtable.loc[lambda dtable: dtable.FREQ == 1, :]
    
    # calculate the future value of this series and add a column to the table
    fv_table = s_interm.assign(FUTURE_VAL = lambda x: x.AMT * np.power(
        discount_rate, rotation - x.AGE))
    
    # calculate the future value by summing the fv_table "FUTURE_VAL" column   
    fut_val = fv_table['FUTURE_VAL'].sum()
    
    # calculate the LEV
    lev = fut_val / (np.power(discount_rate, rotation) - 1) + annual_netrev    
    
    return lev


if __name__ == '__main__':
    print("\n")
    raw_discount = input("What is your discount rate? (enter 6.5 for 6.5%) > ")
    raw_rotation = input("What is your rotation age? > ")
    
    discount = float(raw_discount)/100
    rotation = int(raw_rotation)
    
    lev = round(calc_lev(discount, rotation), 2)
    print("LEV = ${}".format(lev))
    print("\n")
    
    
    
