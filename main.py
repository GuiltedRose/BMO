#!/bin/python
# imports

import os
import sys

# This is the path for the modules the AI has access to.
path = r'tools'

try:
    os.mkdir(path)
    print("Directory for tools created.")
except OSError:
    if os.path.exists(path):
        print("This directory already exists.")
    else:
        sys.exit("Error with file permissions, this user cannot access this directory")
print("Would you like to go into the 'tools' directory?\n")
answer = input("Y/n\n")

yes_choices = ["yes", "y"]
no_choices = ["no", "n"]

if answer.lower() in yes_choices:
    os.chdir(path)
    print(os.getcwd())
elif answer.lower() in no_choices:
    print("Okie Then...")
else:
    print("It's yes or no...")
