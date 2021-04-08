#!/bin/bash
# Send a delete request
curl "$1" -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
