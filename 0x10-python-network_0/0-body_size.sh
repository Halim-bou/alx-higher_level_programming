#!/bin/bash
# size of URL content
curl -sI "$1" | wc -c
