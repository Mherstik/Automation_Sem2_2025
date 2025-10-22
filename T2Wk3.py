## Check modules - import known good module
import os			# interacting with operating system 
import sys			# getting operating system information
import subprocess	# spawn process and get results
import platform

print(platform.platform())
print(platform.system())
print(platform.machine())
print(platform.architecture())
print(platform.node())

import socket
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])



print(os.getenv('COMPUTERNAME'))
print(os.environ)
print(os.environ['OS'])
print(platform.uname())
print(platform.freedesktop_os_release())

# print(os.environ['OS']) # windows only
print(platform.uname())
print(platform.freedesktop_os_release()) # linux only

pl = platform.uname()
print('PL Info is', pl)
print(type(pl))
print(pl.system + ';' + pl.node, pl.release)