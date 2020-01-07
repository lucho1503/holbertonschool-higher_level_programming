#!/bin/bash
#this script send a POST request to the passed URL
curl -s -X POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
