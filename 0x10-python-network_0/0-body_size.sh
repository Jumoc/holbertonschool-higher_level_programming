#!/bin/bash
# Displays the size of the response body
curl -s -w ",%{size_download}\n" "$1" | cut -d "," -f 2
