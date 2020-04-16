#!/usr/bin/python3
# this script send a request to the url and display the value

import sys
from urllib import request

if __name__ == '__main__':

    with request.urlopen(sys.argv[1]) as resp:
        print(resp.headers['X-Request-Id'])
