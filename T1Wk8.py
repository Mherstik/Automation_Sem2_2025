#!/usr/bin/python3
# Name: Week 8 python 
# Author: Marcus H
# Date: 20250903
# Purpose: To teach students stuff
#

def makeNum(userNum):
    try:
        int(userNum)
        print(type(userNum))
    except ValueError:
        print(f"{userNum} is not a number")
    except:
        print("Something went wrong")

makeNum("1")
print("Second")
makeNum(1)
print("Third")
makeNum(1.0)
print("Fourth")
makeNum("Test")
print("Fifth")
makeNum("One")