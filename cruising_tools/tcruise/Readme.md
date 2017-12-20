# Cruising Tools:  tcruise

## Description:
tcruise is a Python package that contains modules to workup timber cruises.
The current version of the package contains a module for variable radius
plots only.  The plan is to include modules for fixed radius plots later.

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



## How to Run the Script:
You will need a recent version of Python (v.3.x) installed on your local machine to run this script.
The scripts require current versions of NumPy and Pandas libraries.  You can pip install these.

1.  Clone the repository
2.  Open a shell (Terminal on Mac, cmd.exe on Windows)
2.  Navigate to the directory where you saved the files.
3.  Start Python from the command prompt.
4.  Import PointSample from the package using.
	```python
	   >>> from tcruise import PointSample
	```
5.  Create a PointSample instance and run the calcs.
	```python
	   >>> ps = PointSample('relative path to pt_data.csv').run()
	   >>> ps
	   	     OUTPUT WILL APPEAR HERE
	```


## Created By:
* Created By:    Springwood Software
* Date:          December 5, 2017
* Email:         jon.lunsford@outlook.com
* License:       MIT


		
	
		