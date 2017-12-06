# Cruising Tools:  n_plots.py

## Description:
n_plots is a Python module (compatible with Python 3.x) that will calculate the number of plots
required by stratum in advance of a timber cruise.  The preliminary cruise information is
added to a data.csv (comma-separated file) and the script does the rest.  The data.csv file can
contain multiple rows, but the column headings and order should not be changed.  Below is a table
showing sample data in the data.csv file, and how it should be represented in the file:

Stratum | Timber_Type_Desc | Est_Vol_Ac | Acres | Est_CV
------- | ---------------- | ---------- | ----- | -------
1		| Pre-Merch Planted| 28			| 20	| 25
2		| Mixed			   | 30			| 35	| 80
3		| Merch Planted	   | 45			| 45	| 20

data.csv:

```text
Stratum, Timber_Type_Desc, Est_Vol_Ac, Acres, Est_CV
1, Pre-Merch Planted, 28, 20, 25
2, Mixed, 30, 35, 80
3, Merch Planted, 45, 45, 20
```

## How to Run the Script:
You will need a recent version of Python (v.3.x) installed on your local machine to run this script.
After installing Python, follow these steps.

1.  Download n_plots.py from this repository.
	
2.  Navigate to the directory where the local 'n_plots.py' file is stored.
			
3.  Enter your stratum data.

	Using File Explorer or MS Excel, open the 'data.csv' file in the n_plots folder.  Enter your
	data and save the file. 
	*If you open using Excel, make sure you re-save the file as a comma-separated, file (.csv) when you 	are finished editing, and do not change the filename.*
	
4.  Enter the following command at the prompt... `python n_plots.py`
		
5.  If no errors occur, the script will ask you for input ('Your desired Sampling Error').

6.  After entering the desired sampling error, press enter.  Your results will be displayed on the screen.


## Created By:
* Created By:    Springwood Software
* Date:          December 5, 2017
* Email:         jon.lunsford@outlook.com
* License:       MIT


		
	
		