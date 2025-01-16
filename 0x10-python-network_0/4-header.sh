#!/bin/bash
# sends a GET req to the URL, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
