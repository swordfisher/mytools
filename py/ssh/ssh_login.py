#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#God is a Rabbit

import wx
import time
import os,sys
import pexpect
import argparse
from lxml import etree

def debug(msg):
    print msg

def exit(msg):
    print msg
    sys.exit(-1)

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,title="wxApp.",size=(0,0),pos=(0,0))
        mm = wx.DisplaySize()
        self.x = mm[0]
        self.y = mm[1]

class App(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show(False)
        return True

class Device(object):
    def __init__(self, args):
        self.host = args.host
        self.cfg = "%s.xml"%(self.host)
        self.port = ""
        self.user = ""
        self.passwd = ""
        self.root_passwd = ""
        self.x = 0
        self.y = 0
        self.p_cfg(self.cfg)
        #self.debug()
        self.auto_login()

    def debug(self):
        msg = '''cfg:%s\nhost:%s\nport:%s\nuser:%s\npasswd:%s\nroot_passwd:%s\n'''\
                %(self.cfg,self.host,self.port,self.user,self.passwd,self.root_passwd)
        debug(msg)

    def get_winsize(self):
        app = App()
        self.x = app.frame.x
        self.y = app.frame.y

    def set_winsize(self, child):
        self.get_winsize()
        child.setwinsize(self.x, self.y)
        return child

    def p_subnode(self, node):
        host = self.host
        if "host" == node.tag:
            host = node.text.strip().rstrip()
        if "port" == node.tag:
            self.port = node.text.strip().rstrip()
        if "user" == node.tag:
            self.user = node.text.strip().rstrip()
        if "passwd" == node.tag:    
            self.passwd = node.text.strip().rstrip()
        if "root_passwd" == node.tag:    
            self.root_passwd = node.text.strip().rstrip()
        if host != self.host:
            exit("host verify failed!\n")

    def p_cfg(self ,cfg):
        tree = etree.parse(cfg)        
        root = tree.getroot()
        for n in root:
            self.p_subnode(n)
    
    def connect(self):
        ssh_cmd = "ssh %s@%s -p %s"%(self.user, self.host, self.port)
        ssh_ret = "%s@%s's password:"%(self.user, self.host)
        child = pexpect.spawn(ssh_cmd)
        if not child.expect([pexpect.TIMEOUT,ssh_ret,pexpect.EOF]):
            exit("auto connect failed!\n")
        return child
    
    def login(self,child):
        child.sendline(self.passwd)
        if not child.expect([pexpect.TIMEOUT,'.*xxxxx360#.*',pexpect.EOF]):
            exit("ssh login failed!\n")
        return child
    
    def chroot(self, child):
        child.sendline('diagnose')
        if not child.expect([pexpect.TIMEOUT, 'Password:.*',pexpect.EOF]):
            exit("diagnose login failed!\n")
        child.sendline(self.root_passwd)
        if not child.expect([pexpect.TIMEOUT,"\[root@xxxxx.*",pexpect.EOF]):
            exit("root passwd error!\n")
        child.interact() 

    def auto_login(self):
        self.chroot(self.set_winsize(self.login(self.connect())))

class process(object):
    def __init__(self):
        pass
    
    def check(self,args, parser):
        if not args.host:
            print parser.print_help()
            sys.exit(-1)

    def process(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--host",dest="host",help="device addr to auto login.")
        args = parser.parse_args()
        self.check(args ,parser)
        d = Device(args)

if __name__=='__main__':
    p = process()
    p.process()

