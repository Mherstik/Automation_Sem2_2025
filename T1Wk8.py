#!/usr/bin/python3
# Name: Week 8 python 
# Author: Marcus H
# Date: 20250903
# Purpose: To teach students stuff
#

def makeNum(user_num):
    """
get userNum and test it
check for type int
third line
"""
    try:
        int(user_num)
        print(type(user_num))
    except ValueError:
        print(f"{user_num} is not a number")
    except:
        print("Something went wrong")

print(makeNum.__doc__)

makeNum("1")
print("Second")
makeNum(1)
print("Third")
makeNum(1.0)
print("Fourth")
makeNum("Test")
print("Fifth")
makeNum("One")


print(help(makeNum))
print(makeNum.__doc__)


