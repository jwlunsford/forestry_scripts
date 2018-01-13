import math
import sys
from collections import namedtuple

def calc_si_1990(htdom, age):
    '''calculates the site index for loblolly pine
    using PMRC-1990 equation 3.3'''
    
    const1 = -1.4128
    const2 = 1.1744
    const3 = 35.3202
    const4 = -4.01832
    
    return math.exp(const1 + const2 * (math.log(htdom) + const3 / age) * math.exp(const4 / age))
    

def calc_si_1996(htdom, age):
    '''calculates the site index for loblolly pine
    using PMRC-1996 equation 13'''
    
    const1 = 0.30323
    const2 = -0.014452
    const3 = 0.8216
    
    return htdom * math.pow(const1 / (1 - math.exp(const2 * age)), const3)


def mean(values):
    '''takes a list of values and returns the mean'''
    return sum(values) / len(values)


if __name__ == "__main__":    
    # store the filename
    filename = sys.argv[1]
    
    # chose a site index equation
    userchoice = input("Choose a site index equation.  Enter 1 for PMRC 1990, or 2 for PMRC 1996 >>> ")
    choice = int(userchoice)
    
    with open(filename) as file:
        header = file.readline().strip().split(', ')
        raw_site_trees = [
            dict(zip(header, line.strip().split(', '))) for line in file]
    
    # create a list of ages, heights and growth from the dictionary
    ages = [int(tree['AGE']) for tree in raw_site_trees]
    hts = [int(tree['HT']) for tree in raw_site_trees]
    grth = [float(tree['5YG']) for tree in raw_site_trees]
    
    mean_age = mean(ages)
    mean_ht = mean(hts)
    mean_grth = mean(grth)
    
    # calculate site index
    if choice == 1:
        si = calc_si_1990(mean_ht, mean_age)
        model = "PMRC 1990"
    elif choice == 2:
        si = calc_si_1996(mean_ht, mean_age)
        model = "PMRC 1996"
    else:
        print("Invalid choice, site index operation cancelled.")
        sys.exit
    
    # print the results to standard out
    print("\n")
    print("    Site Index {} (ba=25): {:2.0f}".format(model, si))
    print("    5 year growth: {:2.2f}".format(mean_grth))
    print("\n")
    
    

        
        