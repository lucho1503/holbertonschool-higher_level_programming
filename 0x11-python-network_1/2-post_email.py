#!/usr/bin/python3
""" this scirpt sends a request and takes a email as argument """

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    url = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(url) as fi:
        print(str(fi.read(), 'utf-8'))
