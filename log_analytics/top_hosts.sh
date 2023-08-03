#!/bin/bash
top_hosts=$(gunzip -c test.log.gz | awk '{print $1}' | sort | uniq -c | sort -rn | head -10 | awk '{print NR "," $2 "," $1}')
echo -e "Rank,Host_IP,Request_Count\n$top_hosts"