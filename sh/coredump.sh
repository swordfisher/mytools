#!/bin/bash

if [ ! $# == 1 ]; then 
echo "Usage: $0 dump-location" 
exit 
fi 

loc=$1

echo "ulimit -S -c unlimited > /dev/null 2>&1" >> /etc/profile
source /etc/profile
echo "1" > /proc/sys/kernel/core_uses_pid
echo "1" > /proc/sys/fs/suid_dumpable
echo "$1/core-%e-%p_%t" > /proc/sys/kernel/core_pattern

