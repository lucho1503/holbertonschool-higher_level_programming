#!/usr/bin/python3
# this script sends a request post and display the response

import sys
from urllib import parse, request


if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    data = parse.urlencode(email)
    data = data.encode('ascii')
    url = request.Request(sys.argv[1], data)
    with request.urlopen(url) as resp:
        print(str(resp.read(), utf-8))
