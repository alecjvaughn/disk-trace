#
# Will take a string disk mount path as input and print 
# the file names and sizes in JSON format.
# Turn on DEBUG for clarifying output
#
# author: Alec Vaughn
#

import sys
import os
from os import path
import pathlib
from pathlib import Path
import json

#
# Method requires a valid mount point string and 
# performs a method call with the path argument
#
def inspectDisk(arg):
    global DEBUG
    p = Path(arg)   # read to path object to perform validation
    if os.path.ismount(p):  # test if disk mount
        if DEBUG == '1':
            print("Valid mount point. PROCESSING...")
        formatOut(p)
    else:
        if DEBUG == '1':
            print("Not a valid mount point. ABORTING...")

#
# Recursively inspects the directory tree with os.walk
# and generates a JSON formatted string and calls json.load, 
# and json.dump respectively, printing the JSON string
#
def formatOut(p):
    global DEBUG
    data = '{"files":[' # begin JSON string, create "files" object
    bCount = 0 # byte count object
    for root, dirs, files in os.walk(p): # recursive scan of directory with standard collections
        for filename in files:
            absFile = root + '/' + os.path.relpath(filename) # full path is required to get size in bytes
            data += '{"%s": %d},' % (absFile, os.path.getsize(absFile)) # add attribute to "files"
            bCount += os.path.getsize(absFile) # add size of file to byte count
    data = data[:-1] # remove comma after last attribute
    data += ']}' # close the JSON object and file
    jsonOut = json.loads(data) # convert JSON string to Python object
    print(json.dumps(jsonOut, sort_keys=True, indent=2, separators=(",", ": "))) # read object here and pretty-print
    if DEBUG == '1':
        print('Bytes used: %d' % (bCount))

DEBUG = sys.argv[2] # debug parameter
inspectDisk(sys.argv[1]) # entry
