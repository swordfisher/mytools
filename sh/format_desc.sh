#!/bin/bash

src=$1 
dst=$2
cat $src | awk '{ $1=""; print $0 }' | sed 's/ .\///' | sed 's/.xml//' | sed 's/ (/ /' | sed 's/)//' > $dst

