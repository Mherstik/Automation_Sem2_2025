#!/usr/bin/env python3
# Description: Get the info

import psutil

def something():
    """Getting something from user
adding some stuff
output stuff + 1"""
    something = input('Give me something: ')
    return something + str(1)

# print(something())
print(something.__doc__)

print(psutil.__doc__)