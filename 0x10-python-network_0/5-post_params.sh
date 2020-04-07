#!/usr/bin/env bash
# this script sends a POST request and display the body response
curl -s -X POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
