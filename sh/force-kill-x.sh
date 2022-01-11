#!/bin/bash

p=$1
ps -ef | grep $p | awk '{print $2}' | xargs -i kill -9 {}

