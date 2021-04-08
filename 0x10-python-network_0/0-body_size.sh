#!/bin/bash
curl -s -w ",%{size_download}\n" 0.0.0.0:5000 | cut -d "," -f 2
