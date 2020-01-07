#!/bin/bash
#this script sends a JSON POST request and display the body
curl -s -H "Content-Type: application/json" "$1" -X POST -d "@$2"
