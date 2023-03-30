#!/bin/bash
#sends a GET request to the URL, and displays the body of the response - only body of a 200 status code response
curl -sL "$1"
