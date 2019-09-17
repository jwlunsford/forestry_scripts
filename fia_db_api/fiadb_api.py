import requests
import json

class EvalidatorQuery:

    def __init__(self, url):
        self.base_url = url

    def eval_group_request(self, state_code=48):
        '''Configure an evalgrp GET request for a particular state.

        Args:
            state_code (int): state code parameter, detault=48 (Texas)

        Returns:
            result (object) - response object from request
        '''
        url = self.base_url + "evalgrp"

        parameters = {
            'schemaName': 'FS_FIADB',
            'whereClause': 'statecd=' + str(state_code),
            'mostRecent=': 'Y'
        }

        # send GET request
        result = self._send_get_request(url, parameters)

        return result


    def ref_table_request(self, table, cols, where):
        '''Configure a table GET request for a particular state and county.

        Args:
            table (str): a valid FIADB table name
            cols (str): table column names separated by commas.
            state_code (int): state code parameter, default=48 (Texas)
            county_code (int): county code parameter, default=347
                               (Nacogdoches)

        Returns:
            result (object) - response object from request
        '''
        if cols is None or table is None:
            print("Please provide a value for all inputs when calling ref_table_request().")
        else:
            url = self.base_url + "refTable"

            parameters = {
                'tableName': str(table),
                'colList': str(cols),
                'whereStr': str(where),
                'outputFormat': 'JSON'
            }

            # send GET request
            result = self._send_get_request(url, parameters)

        return result


    def print_api_response(self, obj):
        '''prints the response object returned by an API request

            Args:
                obj (string): json response object returned by requests

            Returns:
                None: prints json object as text
        '''
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)


    def _send_get_request(self, url, params=None):
        '''send a GET request to the url, with default params = None.

            Args:
                url (str): url string formatted
                params (dict): dictionary of parameters to pass with GET request

            Returns:
                response (object): response object returned from request
        '''
        if not params:
            response = requests.get(url)
        else:
            response = requests.get(url, params=params)

        if response.status_code != 200:
            # invalid response
            return None

        return response



if __name__ == '__main__':
    url_str = "https://apps.fs.usda.gov/Evalidator/rest/Evalidator/"
    qry = EvalidatorQuery(url_str)

    # get a list of eval groups for TEXAS (default STATECD=48)
    result = qry.eval_group_request()
    qry.print_api_response(result.json())

    # query the PLOT ref table.
    qrywhere = 'COUNTYCD=347 AND INVYR=2018'
    result2 = qry.ref_table_request('PLOT', 'COUNTYCD, PLOT', qrywhere)
    qry.print_api_response(result2.json())
    # create a list of plots
    plots = []
    for record in result2.json()['FIADB_SQL_Output']['record']:
        plots.append(record['PLOT'])




