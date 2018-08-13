# Cruising Tools:  PyCruise

## Description:
PyCruise is a Python package that contains modules to workup timber inventories.
The current version of the package contains a module for variable radius
plots only.  The plan is to include modules for fixed radius plots later on.

The program requires plot data to be put into a comma-separated file called
'pt_data.csv'.  Here is a sample of that file:


STD | PLT | SPP | PRD | DBH | THT
----| --- | --- | ----| --- | ---
1	| 1   | 1   | 2   | 10  | 65
1	| 1   | 1	| 2   | 11  | 65
1	| 1   | 1   | 2   | 9   | 65
1   | 1   | 1   | 1   | 10  | 65
...
1   | 2   | 1   | 1   | 10  | 60
1   | 2   | 1   | 1   | 8   | 55
1   | 2   | 1   | 3   | 14  | 75



## How to use PyCruise:
You will need a recent version of Python (3.x) installed on your local machine to use this tool.
The scripts require current versions of NumPy and Pandas libraries.  You can pip install these.

1.  Clone the repository
2.  Open a command prompt (Terminal on Mac, cmd.exe on Windows).
2.  Navigate to the directory where the pycruise package is located.
3.  Start Python in interactive mode from the command prompt.


Sample of how to create a PointSample object, and display volume, basal area, trees per acre and stats.
Assuming that the PyCruise package is stored in a local directory, and Python is
running from this directory.  As a package, PyCruise uses relative imports, so the current directory
needs to contain the top-level directory for the package.  For example if the directory structure
on your machine is 'C:\path\pycruise', then the Python REPL should be run from the path directory.

```
>>> from pycruise import PointSample
>>> ps = PointSample('pycruise/pt_data.csv')  # create a PointSample instance
>>> ps.dope_out()							  # run the calculations
	What is the basal area factor? > 10
	
	Stocking by Species and Product (per acre) ...
	SPP: 1, PRD: 1, TPA: 15.79, BA: 5.00,  VOL: 3.30
	SPP: 1, PRD: 2, TPA: 38.54, BA: 23.33, VOL: 20.20
	SPP: 1, PRD: 3, TPA: 45.31, BA: 41.67, VOL: 37.95
	
	Per acre Stats ....
	
	Trees/Acre : 99.63
	Basal Area/Acre : 70.00
	Mean Tons : 61.45
	Upper Tons : 73.76
	Lower Tons : 49.14
	Std. Deviation : 11.73
	Std. Error : 4.79
	CV% : 19.08
	Sampling Error : 20.03
	
```


## Created By:
* Created By:    Springwood Software
* Date:          December 5, 2017
* Email:         jon.lunsford@outlook.com
* License:       MIT


		
	
		