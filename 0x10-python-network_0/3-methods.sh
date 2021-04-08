#!/bin/bash
# Send a delete request
curl -sI -X OPTIONS "$1" | awk '/Allow: /{print}' | cut -d " " -f 2,3,4
