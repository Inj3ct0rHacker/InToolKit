#!/usr/bin/python
#
# quick installer for !ntoolkit
#
#
from __future__ import print_function
import subprocess
import os
print("[*] Installing requirements.txt...")
subprocess.Popen("pip3 install -r requirements.txt", shell=True).wait()
print("[*] Installing intoolkit to /usr/share/Intoolkit..")
print(os.getcwd())
subprocess.Popen("mkdir /usr/share/Intoolkit/;mkdir /etc/Intoolkit/;cp -rf * /usr/share/Intoolkit/;cp src/core/config.baseline /etc/Intoolkit/intoolkit.config", shell=True).wait()
print("[*] Creating launcher for !ntoolkit...")
filewrite = open("/usr/local/bin/intoolkit", "w")
filewrite.write("#!/bin/sh\ncd /usr/share/Intoolkit\n./intoolkit")
filewrite.close()
print("[*] Done. Chmoding +x.... ")
subprocess.Popen("chmod +x /usr/local/bin/intoolkit", shell=True).wait()
print("[*] Finished. Run 'intoolkit' to start the !nj3ct0r Reverse Engineer Toolkit.")
