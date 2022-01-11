#!/usr/bin/env python

import json

#your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
with open('json.txt', 'r') as handle:
    parsed = json.load(handle)
print(json.dumps(parsed, indent=4, sort_keys=True))

