#!/usr/bin/python3
""" this script sends a request to the URL and display the body """

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        fi = urllib.request.urlopen(sys.argv[1])
        with fi as f:
            print(f.read().decode())
    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
