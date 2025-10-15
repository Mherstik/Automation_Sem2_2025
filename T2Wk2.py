#!/usr/bin/env python3
# Author: MarcusH
# Date: Term 4 2025
# Purpose: To get speed of internet!


## Check modules - import known good module
import os			# interacting with operating system 
import sys			# getting operating system information
import subprocess	# spawn process and get results
import platform

print(sys.executable)

## Import modules
import importlib.util
moduleList = ['requests','time', 'speedtest-cli']
for each in moduleList:
    spec = importlib.util.find_spec(each)
    # print(spec)
    if spec is not None:
        print(f"Module {each} is found")
    else:
        print(f"Module {each} NOT found")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', each])
        print(f"Installed module {each}")

from urllib.request import urlretrieve # built in to python
import requests # requires install
import time

# PSEUDOCODE
# 1) Get URL of file
# 2) Start timer
# 3) Download file
# 4) Stop timer
# 5) Calculate speed
# 6) Save to file/variable for saving later

file2download = "https://github.com/Mherstik/Automation_Sem2_2025/raw/refs/heads/main/50MB.zip"

print("Starting download")
print(f"Downloading file {file2download}")

### start time
starttime = time.time()


### download file
## urllib
## requests
## not recommended - advanced
# BeautifulSoup
# Scrapy

# get file
# response = requests.get(file2download)

## option 2 - using stream
response = requests.get(file2download, stream=True)

### stop time
endtime = time.time()


# test if worked
if response.ok == True:
    dlattempt = "successful"
else: dlattempt = "failed"
# print(response.status_code)

print(f"Download was {dlattempt}.") # \nResponse was {response.status_code}") #, {response.ok}")
print(f"Took {endtime - starttime} seconds")

### Calculate download speed
speed = 50 * 8 / (endtime - starttime)
print(f"{speed:.2f} Mbps")


### Using URL retrieve
print("Using url retrieve")
start2 = time.time()
urlretrieve(file2download)
end2 = time.time()
speed2 = 50 * 8 / (end2 - start2)
print(f"Url retrieve took {end2 - start2:.2f} seconds, was {speed2:.2f} Mbps")




