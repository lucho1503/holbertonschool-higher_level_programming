#!/usr/bin/python3
""" this script takes a string and send a request search star wars API """

import requests
import sys


if __name__ == "__main__":

    response = 'https://swapi.co/api/people/?search={}'.format(sys.argv[1])
    req = requests.get(response)
    req_json = req.json()
    print("Number of results: {}".format(req_json.get('count')))
    for res in req_json.get('results'):
        print(res.get('name'))
