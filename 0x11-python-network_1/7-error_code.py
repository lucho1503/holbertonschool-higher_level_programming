#!/usr/bin/python3

import requests
from requests.exceptions import HTTPError
import sys

if __name__ == "__main__":

    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)

    except HTTPError as error:
        print('Error code: {}'.format(error.response.status_code))
