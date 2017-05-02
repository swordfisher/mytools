import glob
import os
import commands

bin="./rawfile"
core=r"./xx*.core"
filelist=glob.glob(core)
for f in filelist:
    commands.getstatusoutput('gdb --command=fcmd %s %s >> log.core'%(bin ,f))

