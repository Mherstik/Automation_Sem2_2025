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

print(os.getenv('COMPUTERNAME'))
print(os.environ)
print(os.environ['OS'])
print(platform.uname())
print(platform.freedesktop_os_release())