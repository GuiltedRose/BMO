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

# we can maybe move this up higher...
yes_choices = ["yes", "y"]
no_choices = ["no", "n"]

if answer.lower() in yes_choices:
    os.chdir(path)
    print(os.getcwd())
    file = "scanner.py"
    try: 
        open(file, "x")
    except OSError:
        os.path.exists(file)
        print("This file exists, should we append the contents?")
        answer = input("y/n\n")
        if answer.lower() in yes_choices:
            with open(file, "w") as f:
                data = "print('hello world')"
                f.write(data)
elif answer.lower() in no_choices:
    print("Okie, Would you like to list the contents instead?")
    answer = input("y/n\n")
    if answer.lower() in yes_choices:
        os.getcwd(path)
    elif answer.lower() in no_choices:
        print("Okie, would you like to exit?")
        answer = input("y/n\n")
        if answer.lower() in yes_choices:
            sys.exit()
else:
    print("It's yes or no...")
    try:
        with open(file, "w") as f:
            data = ("print('hello world')")
            f.write(data)

    except OSError:
        if os.path.exists(file):
            print("This file exists, would you like to run it?")


