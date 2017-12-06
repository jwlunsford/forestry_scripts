#!/usr/bin/env python 
import math
import sys


def annual_simple_growth(yield1, yield2, periods=5):
    '''Calculates the annual simple growth rate using
    yield @ age 1, yield @ age 2, and years in period'''
    return ((yield2 - yield1) * 100)/(periods * yield1)
    
def calc_future_yield(cur_yield, annual_growth, periods=5):
    '''Calculates the future yield using the annual simple
    growth rate, the current yield and the number of years in period.'''
    return cur_yield * (((annual_growth/100) * periods) + 1)
    
def annual_compound_growth(future_val, current_val, periods=5):
    '''Calculates annual compound growth using cuurent and future value.'''
    annual_exp = 1 / periods
    return math.pow(future_val/current_val, annual_exp) - 1
    
def continue_or_exit():
    '''Prompts the user to choose between continue or exit.'''
    cont = input("Enter 1 to continue or 0 to exit > ")
    if int(cont) == 1:
        return 'continue'
    else:
        return 'quit'


if __name__ == '__main__':
    choice = None
    while choice != 'quit':
        print("Select a calculation...\n")
        calc_choice = input(
            "S) simple annual " 
            "growth, F) future yield, C) compound annual growth, "
            "Q) quit > ")
              
        if calc_choice.lower().strip() == "s":
            # Calculate Simple Annual Growth
            print("This tool calculates the Annual Simple Growth rate of "
                "forest yields.")
            print("- " * 20)
            yield1 = input("Enter the Current Yield or Value (t=1) > ")
            yield2 = input("Enter the Future Yield or Value (t=2) > ")
            if yield2 < yield1:
                print("Future yield/value cannot be less than current yield/value.")
                yield2 = input("Enter the Future Yield or Value (t=2) > ")
            period_length = input("Enter the period (in years) "
                "to evaluate > ")
            simple_growth = annual_simple_growth(float(yield1), float(yield2),
                                                 float(period_length))
            print("\n")
            print("The simple annual growth rate "
                  "for this scenario is {}%".format(round(simple_growth, 2)))
                        
            choice = continue_or_exit()
            
        elif calc_choice.lower().strip() == "f":
            # Calculate Future Value
            print("This tool estimates the future yield of forest stands, "
                "given the, current yield and annual growth rate.")
            print("- " * 20)
            yield1 = input("Enter the current Yield or Value > ")
            ag_rate = input("Enter the simple Annual Growth rate: ")
            period_length = input("How many years into the future do you "
                 "want to evaluate? > ")
            future_yield = calc_future_yield(float(yield1), float(ag_rate),
                                             float(period_length))
            print("\n")
            print("The future yield for this scenario "
                  " is {} (vol/acre)".format(round(future_yield, 2)))
                
            choice = continue_or_exit()
            
        elif calc_choice.lower().strip() == "c":
            # Calculate the compound annual growth
            print("This tool calculates the Annual Compound Growth rate of "
                "forest stands.")
            print("- " * 20)
            cur_val = input("Enter the current value (value can be dollars, "
                "tons, diameter, etc.) > ")
            future_val = input("Enter the future value. > ")
            period_length = input("How many years into the future do you " 
                "want to evaluate? > ")
            compound_growth = annual_compound_growth(float(future_val),
                                                     float(cur_val),
                                                     float(period_length))
            print("\n")
            print("The annual compound growth for this "
                  "scenario is {}%".format(round(compound_growth * 100, 2)))
                
            choice = continue_or_exit()
                
        else:
            sys.exit()
        
            
            
            