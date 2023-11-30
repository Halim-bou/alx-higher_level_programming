#!/usr/bin/env bash
# size of URL content
curl -s "$1" | wc -c
