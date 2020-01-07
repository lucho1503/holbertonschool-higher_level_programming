#!/bin/bash
# this script display all HTTP methods the server will accept
curl -sI OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
