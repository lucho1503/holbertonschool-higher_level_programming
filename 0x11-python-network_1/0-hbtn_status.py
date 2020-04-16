#!/usr/bin/python3
""" this script fetches a request and displayed the body response """


import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as resp:
    response = resp.read()
    print('Body response:\n\t- type: {}\n\t'
          '- content: {}\n\t- utf-8 content: {}'.
          format(type(response), response, response.decode('utf-8')))
