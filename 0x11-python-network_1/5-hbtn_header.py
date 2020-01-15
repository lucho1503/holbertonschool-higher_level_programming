#!/usr/bin/python3
""" this script takes a URL and sends a request to the URL """

import requests
import sys

if __name__ == "__main__":

    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
