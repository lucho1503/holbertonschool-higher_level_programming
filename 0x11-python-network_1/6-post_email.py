#!/usr/bin/python3
""" this script takes a url and email and send post requets """

import requests
import sys

if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    url = requests.post(sys.argv[1], data=email)
    print(url.text)
