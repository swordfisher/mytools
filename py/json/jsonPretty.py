#!/usr/bin/env python

import os,sys
import json

file=sys.argv[1]

with open(file, 'r') as handle:
    parsed = json.load(handle)
print(json.dumps(parsed, indent=4, sort_keys=True))

