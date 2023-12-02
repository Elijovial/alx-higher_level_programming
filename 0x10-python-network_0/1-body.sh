#!/bin/bash
# Takes in a url, sends request to the URL, and displays the body of the response
curl -Lsf "$1"
