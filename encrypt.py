#!/usr/bin/env python2
#Author : ArdiBiz
import tqdm
import time
import os

print "Installing Module....."
os.system("pip2 install tqdm")
os.system("clear")
print "Installing Module Berhasil...."
time.sleep(2)

x = """

    \033[1;31m==========================================================
	\033[1;32m__________                                   _____ 
	___  ____/________________________  ___________  /_
	__  __/  __  __ \  ___/_  ___/_  / / /__  __ \  __/
	_  /___  _  / / / /__ _  /   _  /_/ /__  /_/ / /_  
	/_____/  /_/ /_/\___/ /_/    _\__, / _  .___/\__/
	                             /____/  /_/           
	              \033[1;32m[ \033[1;33mEncrypt File Python V.1 \033[1;32m]
	              	     \033[1;32m[ \033[1;33mArdiBiz \033[1;32m]      
     \033[1;31m=========================================================
	                             
"""
print(x)
print ""
print "\033[1;35m[~] Usage : file.py"
print ""
a = raw_input("\033[1;35m[!] Masukkan File : ")
print ""
print "\033[1;31m[!] Encrypt File "+a
time.sleep(3)
for i in tqdm.tqdm(range(100)):
    time.sleep(0.05)
time.sleep(3)
os.system("python2 -OO -m py_compile "+a+"")
print ""
print "\033[1;35m[+] File Saved : {}o".format(a)
for i in tqdm.tqdm(range(80)):
    time.sleep(0.05)
print ""
time.sleep(4)
print "File Berhasil Di Save !"
time.sleep(3)
exit()