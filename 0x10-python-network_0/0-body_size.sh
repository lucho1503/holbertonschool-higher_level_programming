#!/bin/bash
# this script sends a request to that URL and display the size in bites
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
