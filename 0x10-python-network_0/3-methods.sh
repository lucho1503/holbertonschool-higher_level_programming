#!/usr/bin/env bash
# this script display all methos HTTP
curl -sI OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
