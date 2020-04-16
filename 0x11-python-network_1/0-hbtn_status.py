#!/usr/bin/python3
# this script fetches a request and displayed the body response


from urllib import request

with request.urlopen('https://intranet.hbtn.io/status') as resp:
    response = resp.read()
    print('Body response:\n\t- type: {}\n\t'
          '- content: {}\n\t- utf-8 content: {}'.
          format(type(response), response, response.decode('utf-8')))
