#!/usr/bin/python3
""" this script sends a requests to the URL and pass parameter letter """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        msg = {'q': sys.argv[1]}
    else:
        msg = {'q': ""}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=msg)
    try:
        con = r.json()
        if len(con) > 0:
            print("[{}] {}".format(con.get('id'), con.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
