#!/bin/bash
# status of a request
curl -s -o /dev/null -w "%{http_code}" "$1"
