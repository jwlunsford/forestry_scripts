# Cruising Tools:  n_plots.py

## Description:
n_plots is a Python module (compatible with Python 3.x) that will calculate the number of plots
required by stratum in advance of a timber cruise.  The preliminary cruise information is
added to a data.csv (comma-separated file) and the script does the rest.  The data.csv file can
contain multiple rows, but the column headings and order should not be changed.  Below is a table
showing sample data in the data.csv file, and how it should be represented in the file:

Stratum | Timber_Type_Desc | Est_Vol_Ac | Acres | Est_CSV
------- | ---------------- | ---------- | ----- | -------
1		| Pre-Merch Planted| 28			| 20	| 25
2		| Mixed			   | 30			| 35	| 80
3		| Merch Planted	   | 45			| 45	| 20

data.csv:

```text
Stratum, Timber_Type_Desc, Est_Vol_Ac, Acres, Est_CSV
1, Pre-Merch Planted, 28, 20, 25
2, Mixed, 30, 35, 80
3, Merch Planted, 45, 45, 20
```

## How to Run the Script:
You will need a recent version of Python (v.3.x) installed on your local machine to run this script.
After installing Python, follow these steps.

1.  Download and extract the script files.
	
	In a browser type the following address.
		https://github.com/jwlunsford/forestry_scripts.git
	
	
	Download the files as a Zip package.  Save and extract the files to your local machine.
	
2.  To run the python scripts, you will need to open a command prompt and navigate to the directory
	where you extracted the files.
	
	On Windows:  Assuming you extracted the files to the C:\forestry_scripts directory.  At the command
	prompt type the following:
		> `cd C:\forestry_scripts\cruising_tools\n_plots`
			
	On Mac/Unix:  Assuming you extracted the files to your Documents folder.  At the Terminal prompt type
	the following:
		$ `cd ~/Documents/cruising_tools\n_plots`
			
3.  Enter your stratum data.

	Using Windows Explorer, or Finder (Mac), open the 'data.csv' file in the n_plots folder.  You can open
	the file using a plain text editor such as Notepad, or using MS Excel.  *If you open using Excel, make
	sure you re-save the file as a comma-separated, file (.csv).  Enter your data.
	
4.  Run the script.
	
	From the command-line run the script using the python command.  *Make sure you are still in the n_plots directory.  This would be the same command in Mac Terminal*
		C:\...> python n_plots.py
		
5.  If no errors occur, the script will prompt you for input ('Your desired Sampling Error').

6.  Type the input for Sampling Error and press Enter.  Your results will be displayed on the screen.


## Created By:
Jon W. Lunsford - Springwood Software
December 5, 2017
jon.lunsford@outlook.com


		
	
		