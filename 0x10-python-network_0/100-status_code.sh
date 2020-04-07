#!/usr/bin/env bash
#this script sends a request and display the status code
curl -so /dev/null -w "%{http_code}" "$1"
