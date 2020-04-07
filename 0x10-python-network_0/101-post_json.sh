#!/usr/bin/env bash
#this script sends a json POST request and display the body response
curl -s -H "Content-Length: application/json" "$1" -X POST -d "@2"
