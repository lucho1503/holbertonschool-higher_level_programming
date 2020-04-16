#!/usr/bin/python3
# this script fetchs a request and displayed the body response

import requests

if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    url = r.text
    print('Body response:\n\t- type: {}\n\t'
          '- content: {}'.format(type(url), url))
