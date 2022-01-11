#!/bin/bash

process=$1
log=cpu-usage.log
echo "" > $log

while true 
do	
		cpu=$(top -p $(pgrep -d, $process) -n 1  | awk '{print $9}' | sed -n '8,$p' | awk '{sum += $1};END {print sum}') 
	   	echo "current cpu = "$cpu 
		echo $cpu >> $log
		cat $log | awk '{sum+=$1} END {print "Average = ", sum/NR}'
		echo -e
		sleep 1
done
