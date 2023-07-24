#!/bin/python
# imports

import os

# This is the path for the modules the AI has access to.
path = r'tools'

if os.getcwd() != path and path == False:
    os.mkdir(path)
    os.chdir(path)
elif os.getcwd() != path and path == True:
    os.chdir(path)
else:
    os.chdir(path)

print(os.getcwd())
