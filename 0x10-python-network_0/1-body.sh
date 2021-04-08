#!/bin/bash
# Displays the body of a response if status equals 200
status=$(curl -LsI "$1" | tail -6 | head -1 | cut -d " " -f 2)
if [ "$status" == "200" ]; then
    curl -sL "$1"
fi
