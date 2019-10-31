# datetime module is contained within Python's standard library
# The datetime submodule is contained within the datetime module
# A collection of related functions makes up a module, and there are many modules in the standard library
# There are also tons of thrid-party modules which are built and maintained by the Python community - explore http://pypi.python.org
#Python standard library docs can be found at https://docs.python.org/3/library/index.html

from datetime import datetime
from datetime import date
from os import getcwd
from sys import platform
from sys import version
from os import environ
from os import getenv
import time
# import sys
# import os

odds = [1,3,5,7,9,
        11,13,15,17,19,
        21,23,25,27,29,
        31,33,35,37,39,
        41,43,45,47,49,
        51,53,55,57,59]

right_this_minute = datetime.today().minute

# blocks (or suites) in Python are always indented
if right_this_minute in odds:
    print(right_this_minute)
    print("This minute seems a bit odd")
else:
    print("Not an odd minute")

current_day = time.strftime("%A")
print(current_day)
if current_day == 'Saturday':
    print("Time to go to the movies.")
elif current_day == 'Sunday':
    print("Time to go to church.")
else:
    print("Time to go to work.")

print("What Platform am I running on?")
#print(sys.platform)
print(platform)

print("What version of Python am I running?")
print(version)
#print(sys.version)

print("What path am I currently running this code from?")
where_am_I = getcwd()
print(where_am_I)

print("What are all of my environment variables?")
print(environ)
#print(os.environ)

print("What is my HOME directory?")
print(getenv('HOME'))
#print(os.getenv('HOME'))

print("What is the current date and time?")
print(datetime.today())
print(datetime.isoformat(datetime.today()))
print(time.strftime("%H:%M %A %p"))