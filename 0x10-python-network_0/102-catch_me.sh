#!/bin/bash
#request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -s -w "You got me!" "$1"
