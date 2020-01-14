#!/usr/bin/python3
""" this script fetches a request """


import urllib.request

with urllib.request.urlopen("https://intranet.hbtn.io/status") as fi:

    url = fi.read()
    print('Body response:\n\t- type: {}\n\t'
          '- content: {}\n\t- utf8 content: {}'
          .format(type(url), url, url.decode('utf-8')))
