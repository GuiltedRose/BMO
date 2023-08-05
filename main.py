#!/bin/python
# imports

import os
import sys

# This is the path for the modules the AI has access to.
path = ""
running = True

# making decisions
yes_choices = ["yes", "y"]
no_choices = ["no", "n"]

while running == True:
    answer = input("Would you like to make a directory?")
    if answer.lower() in yes_choices:
        path = input("Please provide a directory name.")
        os.mkdir(path)
    elif answer.lower() in no_choices:
        print("Goodbye then ^^")
        running = False
        sys.exit()

