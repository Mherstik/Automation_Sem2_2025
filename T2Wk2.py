#!/usr/bin/env python3
# Author: MarcusH
# Date: Term 4 2025
# Purpose: To get speed of internet!

## Import modules
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
response = requests.get(file2download)

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
speed = 50 * 8 /(endtime - starttime)
print(f"{speed:.2f} Mbps")


