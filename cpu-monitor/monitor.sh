#!/bin/bash

log=cpu-usage.log
echo "" > $log

while true 
do	
		cpu=$(top -p $(pgrep -d, serverids) -n 1  | awk '{print $10}' | sed -n '8,$p' | awk '{sum += $1};END {print sum}') 
	   	echo "current cpu = "$cpu 
		echo $cpu | tee >> $log
		cat $log | awk '{sum+=$1} END {print "Average = ", sum/NR}'
		echo -e
		sleep 1
done
