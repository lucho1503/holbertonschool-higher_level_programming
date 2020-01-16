#!/usr/bin/python3
""" thsi script takes a credentiales of my github and display the id """

from requests import *
import sys

if __name__ == "__main__":

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    req = get(url, auth=auth.HTTPBasicAuth(username, password))
    req_json = req.json()
    print(req_json.get('id'))
