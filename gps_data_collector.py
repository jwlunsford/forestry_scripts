# Module to Process Data from the comment field in a Garmin GPSMap device
# Created: 1/1/2020
# By: Jon Lunsford, Springwood Software

# imports
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib as plt
import argparse
import sys
import os


def load_gps_data(fname):
    """load gps data into a GeoDataFrame

    Args:
        fname:  path to the file, only .SHP allowed at this time.

    Returns:
        A GeoDataFrame loaded with SHP attributes
    """
    data_out = gpd.read_file(fname)
    return data_out


def extract_comment(row):
    """creates a Pandas Series using the data in the comment field

    Args:
        row: row of data from a GeoDataFrame

    Returns:
        Pandas Series with keys planted_count, and natural_count
    """
    a, b = row.split('/')
    return pd.Series({'planted_cnt': int(a), 'natural_cnt': int(b)})


def calc_plots(data, factor):
    """outputs the results of survival plots with stats.

    Args:
        data: GeoDataFrame with planted_cnt and natural_cnt fields
        factor: Plot expansion factor to use in calculations.

    Returns:
        results: results stored in a dictionary
    """
    if isinstance(data, gpd.GeoDataFrame):
        results = {}
        # calculate means (multiply by the expansion factor)
        planted_mean = round(data['planted_cnt'].mean() * factor, 0)
        natural_mean = round(data.natural_cnt.mean() * factor, 0)

        # calculated stats for planted trees
        planted_std = round(data.planted_cnt.std() * factor, 0)
        planted_std_err = round(planted_std / data.planted_cnt.count() ** 0.5, 2)
        planted_ci_lower = round(planted_mean - 2 * planted_std_err, 0)
        planted_ci_upper = round(planted_mean + 2 * planted_std_err, 0)
        planted_cv = round((planted_std / planted_mean) * 100, 2)
        planted_sample_err = round((2 * planted_std_err / planted_mean) * 100, 2)

        # add calcs to results dict and return
        results['Planted MEAN'] = planted_mean
        results['Natural MEAN'] = natural_mean
        results['Planted STD'] = planted_std
        results['Planted STD ERR'] = planted_std_err
        results['Planted CI (lower)'] = planted_ci_lower
        results['Planted CI (upper)'] = planted_ci_upper
        results['Planted CV%'] = planted_cv
        results['Planted SMP ERR%'] = planted_sample_err

        return results

    else:
        return None


def format_geodata(gdf):
    '''process the raw DataFrame into only what is required for output'''

    # extract only the columns we are interested in working with
    base_data = gdf[['ident', 'Latitude', 'Longitude', 'comment', 'geometry']].copy()

    # copy the contents of 'comment' field to two new fields in the GDF
    base_data[['planted_cnt', 'natural_cnt']] = base_data.apply(lambda x: extract_comment(x['comment']), axis=1)

    # return
    return base_data


def main():

    parser = argparse.ArgumentParser(description='Calculate survival plots from GPS data.')

    parser.add_argument('input',
                        metavar='INPUT_DIR',
                        type=str,
                        help='input folder path for recursive processing of SHPs')

    parser.add_argument('factor',
                        metavar='EXP_FACTOR',
                        type=int,
                        help='plot expansion factor (Ex.; 50 or 100)')

    # execute parse args
    args = parser.parse_args()

    input = args.input
    factor = args.factor

    # list of dicts, returned from calc_plots()
    out_data = list()

    try:
        #for filenames in this directory
        for filename in os.listdir(input):
            if filename.lower().endswith('shp'):
                # get the filename minus the extension, can add another split to remove the extension
                job_name = filename.split('/')[-1]

                # convert the SHP to a GeoDataFrame
                raw_data = load_gps_data(input + filename)

                # format to minimal data required for processing
                data = format_geodata(raw_data)

                # output results
                output_dict = calc_plots(data, factor)
                output_dict['job_name'] = job_name
                out_data.append(pd.Series(output_dict))

        # output data
        d_out = pd.DataFrame(out_data)
        d_out.to_csv(input + "Survival_Plot_Summary.csv")

        print(f'EXPORT COMPLETE!  Survival_Plot_Summary.csv was exported to {input}')

    except:
        print("ERROR: Failed to process the shapefiles. Please verify entry or use -h in command for help.")


if __name__ == '__main__':
    #input = '/fake/url/path'
    #factor = 50
    main()



