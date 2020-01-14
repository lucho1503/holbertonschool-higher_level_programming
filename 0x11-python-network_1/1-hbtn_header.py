#!/usr/bin/python3
""" thus script sends a request to the URL and display the value """

import sys
import urllib.request

if __name__ =="__main__":

    with urllib.request.urlopen(sys.argv[1]) as fi:
        print(fi.headers['X-Request-Id'])
