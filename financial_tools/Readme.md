# Yields.py
This script contains three functions.

1.  An annual simple growth rate calculator.
	This calculates the annual growth rate using the simple interest formula.  Values can be in
	any format as long as they are numeric (e.g.; dollars, tree diameter inside bark, yields/acre, etc.)
	
	Example: When to harvest?  If the average annual growth rate exceeds your alternative rate of return, (i.e.; the return you could get elsewhere) then hold.  Otherwise, harvest.
	
	```text
	Current stumpage value/acre = $1800
	Future (expected) stumpage value/acre = $2500
	Ratio of future to present value = 1.4
	Evaluation Period = 5 years
	Average Annual Growth Rate = ((1.4)^1/5) - 1) x 100 = 7%
	```
	
2.  A future yield calculator.
	Given the rate of simple interest and current yield, this calculates the future yield.
	
3.  An annual compound growth rate calculator.
	This calculates the annual compound rate of growth given a current value, future value and number
	of periods.  Again, values can be in any numeric format (e.g. they can represent dollars,
	tree diameters, yields/acre, etc.)
	
# Forest_Finance.py
This script contains one function - calc_lev().

1.  calc_lev() - calculates the Land Expectation Value of a managed stand using cost and revenue
    data supplied by the user.  Costs may include establishment, intermediate treatments, and annual expenses.  Revenues may include funds from thinning, harvest, and leases.
	
2.  Use the provided CSV file to enter an itemized list of costs and revenues.  This file should be named lev_data.csv and needs to be in the current directory where the script is executed.  Below is an example of the CSV file.

	AGE | DESC        | FREQ | AMT
	--- | ----------- | ---- | ---
	0   | Ad Valorem  | 0    | -3
	0   | Hunting Rev | 0    | 10
	0   | Stand Est.  | 0    | -250
	15  | Thinning Rev| 1    | 200
	28  | Harvest Rev | 1    | 1800
	
	* Revenues should be entered as positive values, costs as negative values
	* AGE = the stand age when the event occurs - for annual costs or expenses use 0 in the AGE column
	* DESC = short description of the event
	* FREQ = frequency of the event, use 0 for annually recurring events and 1 for a one time event
	* AMT = cost or revenue amount in dollars
	
	

# Run the programs
To run the program from the command line prompt.

1.  Download a copy of the file from the repository.
2.  Navigate to the directory where the local script (.py) file is stored.
3.  Enter the following command at the prompt... `python <filename>.py`


# Created By:
* Created by:  Springwood Software
* Date:		   December 5, 2017
* Email:       jon.lunsford@outlook.com
* License:     MIT
