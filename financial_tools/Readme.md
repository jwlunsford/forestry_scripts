# Yields.py
This script contains three functions.

1.  An annual simple growth rate calculator.
	This calculates the annual growth rate using the simple interest formula.  Values can be in
	any format as long as they are numeric (e.g.; dollars, tree diameter inside bark, yields/acre, etc.)
	
	Example: When to harvest?  If the average annual growth rate exceeds your alternative rate of return, then hold.  Otherwise, harvest.
	
	```text
	Current stumpage value/acre = $1800
	Future (expected) stumpage value/acre = $2500
	Ratio of future to present value = 1.4
	Evaluation Period = 5 years
	Rate of Return = ((1.4)^1/5) - 1) x 100 = 7%
	```
	
2.  A future yield calculator.
	Given the rate of simple interest and current yield, this calculates the future yield.
	
3.  An annual compound growth rate calculator.
	This calculates the annual compound rate of growth given a current value, future value and number
	of periods.  Again, values can be in any numeric format (e.g. they can represent dollars,
	tree diameters, yields/acre, etc.)
	

# Run the program
To run the program from the command line prompt.

1.  Download a copy of the file from the repository.
2.  Navigate to the directory where the local 'yields.py' file is stored.
3.  Enter the following command at the prompt... `python yields.py`


# Created By:
* Created by:  Springwood Software
* Date:		   December 5, 2017
* Email:       jon.lunsford@outlook.com
* License:     MIT
