#!usr/bin/env python

import pandas as pd
import numpy as np


def calc_lev(rate=0.04, rotation=30):
    """Calculate the Land Expectation Value.

    Keyword arguments:
    rate -- alternative rate of return expressed as a percentage
    rotation -- stand rotation in years
    """
    discount_rate = 1 + rate

    dtable = pd.read_csv('lev_data.csv')  # read the csv into a Pandas dataframe

    # get the annual cost/revenue series data, denoted by FREQ = 0
    s_annual = dtable.loc[lambda dtable: dtable.FREQ == 0, :]

    # sum the annual expenses, ASSUMES the annual expenses have the same length of years
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

def calc_npv(rate=0.04, inflation=0.01):
    """Calculates the Net Present Value.

    Keyword Arguments:
    rate = alternative rate of return expressed as a percentage.  Default=0.04
    """
    discount_rate = 1 + rate
    inflation_rate = 1 + inflation

    dtable = pd.read_csv('lev_data.csv') # read the csv into a dataframe

    # calculate the Future Value of the cashflows and append to the dtable
    dtable = dtable.assign(FVAL = lambda x: x.AMT * np.power(inflation_rate, x.AGE))

    # GET INTERMEDIATE CASH FLOWS:
    # filter the intermediate cost/revenue series, denoted by FREQ=0
    interm_data = dtable.loc[lambda dtable: dtable.FREQ == 1, :]

    # calculate and append the Present Value to the interm_data table
    interm_data = interm_data.assign(PVAL = lambda x: x.FVAL * np.power(discount_rate, np.negative(x.AGE)))

    interm_cash_flow_sum = interm_data['PVAL'].sum()

    # GET ANNUAL CASH FLOWS:
    # filter the annual cost/revenue series, denoted by FREQ=1
    annual_data = dtable.loc[lambda dtable: dtable.FREQ == 0, :]

    # calculate and append the Present Value to the annual_data table
    annual_data = annual_data.assign(PVAL = lambda x: x.AMT * (np.power(discount_rate, x.AGE) - 1) / (rate * np.power(discount_rate, x.AGE)))

    annual_cash_flow_sum = annual_data['PVAL'].sum()

    npv = interm_cash_flow_sum + annual_cash_flow_sum

    return npv


if __name__ == '__main__':
    print("\n")
    raw_discount = input("What is your discount rate? (enter 6.5 for 6.5%) > ")
    raw_inflation = input("What is the expected inflation rate? (enter 2.0 for 2%) > ")
    raw_rotation = input("What is your rotation age? > ")
    raw_scenario = input("What would you like to name this scenario? > ")

    # convert user input to appropraiate values
    discount = float(raw_discount)/100
    inflation = float(raw_inflation)/100
    rotation = int(raw_rotation)

    lev = round(calc_lev(discount, rotation), 2)
    npv = round(calc_npv(discount, inflation), 2)


    print("Scenario {}".format(raw_scenario))
    print("Land Expectation Value (LEV) = ${}".format(lev))
    print("Net Present Value (NPV) = ${}".format(npv))
    print("\n")



