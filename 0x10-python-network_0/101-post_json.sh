#!/bin/bash
# Post a file contents
curl -s -d "@$2" -X POST "$1"
