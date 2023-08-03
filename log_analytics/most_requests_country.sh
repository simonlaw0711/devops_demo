#!/bin/bash

read num_requests country_name <<< $(gunzip -c test.log.gz | awk '{print $1}' | sort | uniq | while read IP; do echo $(geoiplookup $IP); done | awk -F': ' '{print $2}' | sort | uniq -c | sort -rn | head -1)

echo "The country that made the most HTTP requests is: $country_name"
echo "$num_requests requests have been made"