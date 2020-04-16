#!/usr/bin/python3
# this script sends a POST request to URL passed with email as a parameters

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}

    res = requests.post(url, data=email)
    print(res.text)
