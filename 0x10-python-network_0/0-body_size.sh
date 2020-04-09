#!/bin/bash
# this script sends a request to URL and display the body size
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
