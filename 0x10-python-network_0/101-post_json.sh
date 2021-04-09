#!/bin/bash
# Post a file contents
curl -X POST "$1" -d @"$2" --header "Content-Type: application/json"
