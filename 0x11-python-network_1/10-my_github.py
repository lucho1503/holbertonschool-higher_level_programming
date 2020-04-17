#!/usr/bin/python3
# this script takes a credentials of mi github account and display id

from requests import *
import sys

if __name__ == "__main__":

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    res = get(url, auth=auth.HTTPBasicAuth(username, password))
    res_json = res.json()
    print(res_json.get('id'))
