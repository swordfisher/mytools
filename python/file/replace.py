#!/usr/bin/python
# -*- coding: utf-8 -*-
#God is a Rabbit

import os,sys
#from pathlib import Path
#import glob

def debug(s):
    print 'debug:%s'%s

def write(f, lines):
    d_path = f + '.replace'
    d_fd = open(d_path,'w')
    d_fd.writelines(lines)
    d_fd.close()
    debug(d_path)
    #debug(lines)
    return d_path

def source(f):
    fd = open(f)
    lines = fd.readlines()
    fd.close()
    return lines

def mv(d,s):
    cmd = "mv %s %s -f"%(d, s)
    os.system(cmd)

def replace(fpath):
    lines = source(fpath)
    wlines = []
    for l in lines:
        if s in l: 
            l = l.replace(s,d) 
        wlines.append(l)
    mv(write(fpath, wlines), fpath)

def remove(p):
    cmd = 'find %s -name "*.replace" |xargs -i rm {}'%(p)
    os.system(cmd)

def walk(path):
    for fpath,dirs,fs in os.walk(path):
        for f in fs:
            full = os.path.join(fpath,f)
            if 'svn' in full: continue
            replace(full)

if __name__=='__main__':
    s = sys.argv[1]
    d = sys.argv[2]
    p = sys.argv[3]
    remove(p)
    walk(p)
