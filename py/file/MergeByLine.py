#!/usr/bin/env python

import os,sys

def Strip(s):
    return s.strip().rstrip()

def ReadLinesFromFile(path):
    with open(path) as f:
        r = f.readlines()
        #f.close()
    return r

def MergeByLine(a, b):
    alines = ReadLinesFromFile(a)
    blines = ReadLinesFromFile(b)
    assert len(alines) == len(blines)
    for i in range(len(alines)):
        print Strip(alines[i]) + '  ' + Strip(blines[i])
    return

def CheckArg():
    if len(sys.argv) != 3:
        print 'argv error!'
        sys.exit(-1)

if __name__=='__main__':
    CheckArg()
    a = sys.argv[1]
    b = sys.argv[2]
    MergeByLine(a, b)
