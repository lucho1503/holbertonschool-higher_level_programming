#!/usr/bin/python3
# this script sends a POST reqeusts with a letter as a parametersimport sys

import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) > 1:
        msj = {'q': sys.argv[1]}
    else:
        msj = {'q': ""}

    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=msj)

    try:
        res = r.json()
        if len(res) > 0:
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
