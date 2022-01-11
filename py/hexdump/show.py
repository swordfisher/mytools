
import os,sys
import hexdump

def read(file):
    f = open(file)
    buff = f.read()
    #print buff
    return buff

def show(buff):
    print "raw header len: %d\n"%len(buff)
    print hexdump.hexdump(buff)    

if len(sys.argv) != 2:
    print "argc error"
    sys.exit(-1)
show(read(sys.argv[1]))
