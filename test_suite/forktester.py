#!/usr/bin/env python
import subprocess
import sys
import threading
import os
base_dir = os.path.dirname(sys.argv[0])
if len(sys.argv) > 1:
    jpg_name = sys.argv[1]
else:
    jpg_name = os.path.join(base_dir, "..", "images", "iphone.jpg")

proc = subprocess.Popen(['./lepton','-fork'],
                        stdout=subprocess.PIPE,
                        stdin=subprocess.PIPE)
valid_fds = []
valid_names = []
for i in range(4):
    valid_names.append((proc.stdout.readline().strip(),
                        proc.stdout.readline().strip()))
    valid_fds.append((open(valid_names[-1][0],'w'),
                      open(valid_names[-1][1],'r')))

def add4():
    for i in range(4):
        valid_names.append((proc.stdout.readline().strip(),
                            proc.stdout.readline().strip()))
        valid_fds.append((open(valid_names[-1][0],'w'),
                          open(valid_names[-1][1],'r')))

with open(jpg_name) as f:
    jpg = f.read()
def fn():
    valid_fds[0][0].write(jpg)
    valid_fds[0][0].close()
def fn1():
    valid_fds[1][0].write(dat)
    valid_fds[1][0].close()
u=threading.Thread(target=add4)
u.start()
t=threading.Thread(target=fn)
t.start()

dat = valid_fds[0][1].read()
valid_fds[0][1].close()
t.join()
print len(jpg),len(dat)
v=threading.Thread(target=fn1)
v.start()
ojpg = valid_fds[1][1].read()
valid_fds[1][1].close()
t.join()

assert ojpg == jpg

print 'yay',len(ojpg),len(dat),len(dat)/float(len(ojpg))
u.join()
