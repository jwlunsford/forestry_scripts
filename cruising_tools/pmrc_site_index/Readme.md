# Cruising Tools:  PMRC Site Index Calculator

## Description:
Pmrc_si.py is a script that will allows easy Site Index calculations from data collected in the field.
The current version is only compatible with PMRC-1990 and PMRC 1996 site index equations, but
others will be added later if needed.  The idea here is that a cruiser is collecting site index
trees (e.g. one per plot) as they are cruising a planted stand of Loblolly pine timber.  The model
can be used for pre-merch calculations as well, but below about age 7 they may not be very accurate.

The inputs to these models are dominant height and age.
Dominant height and age are calculated directly from the data by averaging the values found in the
companion data file.  Data needs to be entered into plotdata.csv prior to running the tool.

Here is a sample of the 'plotdata.csv' file:

AGE | HT | 5YG
--- | -- | ---
23  | 70 | 1.2
22  | 74 | 1.1
24  | 79 | 1.2
22  | 84 | 1.1

The '5YG' field is for 5 year growth increments taken from a core sample.  These values are NOT optional, so
if you want to exclude growth data then zero out the values in this column.

## How to use PMRC_SI:
You will need a recent version of Python (3.x) installed on your local machine.
The script requires math and sys modules, which are included in the standard package.

1.  Clone the repository
2.  Navigate to the repository directory using a shell prompt
3.  Run the following command from the shell
	`
	$ python pmrc_si.py plotdata.csv
	`
	(make sure to enter the filename at the end of the command)
	
## Created By:
* Created By:    Springwood Software
* Date:          January 13, 2018
* Email:         jon.lunsford@outlook.com
* License:       MIT