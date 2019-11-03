# FIA DB API

This project includes a python module with scripts to access the [USDA FIA Database
API](https://www.fia.fs.fed.us/tools-data/).  The code has an object called
EvalidatorQuery which is used to access the server.

[Database Documentation FIADB 8.0 Phase2](https://www.fia.fs.fed.us/library/database-documentation/index.php)

## Requirements

The current version of this tool requires the following modules.

* requests v2.22.0
* json (included with Python 3.6 standard library)

## Example Workflow

  # create a query object

  ```python
  qry = FIAQuery()
  ```

  Query 1:  get a list of eval groups for TEXAS (default STATECD=48)

  ```python
  result = qry.eval_group_request()
  qry.print_api_response(result.json())
  ```

  Query 2:  get the PLOT ref table based on the evalgrp '482018'

  ```python
  qrywhere = 'COUNTYCD=347 AND INVYR=2018'
  result2 = qry.ref_table_request('COND', 'COUNTYCD, PLOT, TRTCD1, TRTCD2, TRTCD3', qrywhere)
  qry.print_api_response(result2.json())
  ```

  Put the resulting plot data into a list of dictionaries

  ```python
  plots = list()
  for record in result2.json()['FIADB_SQL_Output']['record']:
      print(record)
      plots.append(record)
  ```

## Created By:

* Created By: Springwood Software
* Date: September 16, 2019
* Email: jon.lunsford@outlook.com
