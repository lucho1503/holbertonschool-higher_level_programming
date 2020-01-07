#!/bin/bash
#this script sent a header variable with the value 98
curl -Ls "$1" -H "X-HolbertonSchool-User-Id: 98"
