#!/bin/bash
# status of a request
curl -LsI "$1" | tail -6 | head -1 | cut -d " " -f 2
