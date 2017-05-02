import glob
import os
import commands

filelist=glob.glob(r'./serverids*.core')
bin="./rawfile"
for f in filelist:
    commands.getstatusoutput('gdb --command=fcmd %s %s >> log.core'%(bin ,f))

