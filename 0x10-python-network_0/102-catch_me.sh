#!/bin/bash
#this script makes a request that causes the server respond with message
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin:HolbertonSchool"
