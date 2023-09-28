#!/bin/bash

# Check if the script is provided with a URL argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command-line argument
URL=$1

# Send a GET request using curl and display the body if the status code is 200
response=$(curl -s -o /dev/null -w "%{http_code}" "$URL")

if [ "$response" -eq 200 ]; then
  curl -s "$URL"
else
  echo "Error: HTTP Status Code $response"
fi
