#!/bin/bash
total_requests=$(gunzip -c test.log.gz | awk '{print $1}' | wc -l | awk '{print $1}')
echo "The total number of HTTP requests recorded in the log file is: $total_requests"