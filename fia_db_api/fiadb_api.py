import requests
import json

class EvalidatorQuery:

    def __init__(self, url):
        self.base_url = url

    def eval_group_request(self, state_code=48):
        '''Configure an evalgrp GET request.

        Args:
            state_code (int): state code parameter, detault = 48 (Texas)

        Returns:
            None - prints API results to the standard output
        '''
        url = self.base_url + "evalgrp"

        parameters = {
            'schemaName': 'FS_FIADB',
            'whereClause': 'statecd = 48',
            'mostRecent=': 'Y'
        }

        result = self._send_get_request(url, parameters)
        print(f'Status Code: {result[0]}')
        self._print_api_response(result[1].json())


    def _print_api_response(self, obj):
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
                status_code, response (tuple): status code and response object
        '''
        if not params:
            response = requests.get(url)
        else:
            response = requests.get(url, params=params)

        return response.status_code, response



if __name__ == '__main__':
    url_str = "https://apps.fs.usda.gov/Evalidator/rest/Evalidator/"
    qry = EvalidatorQuery(url_str)
    qry.eval_group_request()





