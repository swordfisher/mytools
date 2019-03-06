#!/usr/bin/env python

import os,sys

##### 
def Strip(s):
    return s.strip().rstrip()

def ReadLinesFromFile(path):
    with open(path) as f:
        r = f.readlines()
        #f.close()
    return r

##### 
def EchoFile(t):
    with open('./translate_rule_list', 'w') as f:
        for x in t: f.writelines(x + '\n')

def FindTranslate(all, no, ignore):
    FindNotInBCInA(all, no, ignore)

def FindNotInBCInA(all, no, ignore):
    a, n, i = FilterRuleId(all, no, ignore)
    #print a
    #print n
    #print i
    t = [x  for x in a if x not in n and x not in i]
    print len(t)
    EchoFile(t)

def FilterRuleId(all, no, ignore):
    alines = ReadLinesFromFile(all)
    nlines = ReadLinesFromFile(no)
    ilines = ReadLinesFromFile(ignore)
    all_rules = [Strip(x).split()[0] for x in alines] 
    no_rules = [Strip(x).split()[0] for x in nlines]
    ignore_rules = [Strip(x).split()[0] for x in ilines]
    return all_rules, no_rules, ignore_rules 

def CheckArgs():
    assert len(sys.argv) == 4

def FindTranslateRule():
    CheckArgs()
    all = sys.argv[1]
    no = sys.argv[2]
    ignore = sys.argv[3]
    FindTranslate(all, no, ignore)
#####

def FindTranslateHighLevel(translate, high):
    FindAInB(translate, high) 

def FindAInB(a, b):
    alines = ReadLinesFromFile(a)
    blines = ReadLinesFromFile(b)
    arules = [Strip(x).split()[0] for x in alines]
    brules = [Strip(x).split()[0] for x in blines]
    #print arules
    #print brules
    result = [x for x in brules if x in arules]   
    print result
    print len(result)

def FindHighTranslateRule():
    translate = sys.argv[1]
    high = sys.argv[2]
    FindTranslateHighLevel(translate, high)
    
#####

if __name__=='__main__':
    #FindTranslateRule()
    FindHighTranslateRule()
