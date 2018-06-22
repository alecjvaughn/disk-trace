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
    p = Path(arg)
    if os.path.ismount(p):
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
    data = '{"files":['
    bCount = 0
    for root, dirs, files in os.walk(p):
        for filename in files:
            absFile = root + '/' + os.path.relpath(filename)
            data += '{"%s": %d},' % (absFile, os.path.getsize(absFile))
            bCount += os.path.getsize(absFile)
    data = data[:-1]
    data += ']}'
    jsonOut = json.loads(data)
    print(json.dumps(jsonOut, sort_keys=True, indent=2, separators=(",", ": ")))
    if DEBUG == '1':
        print('Bytes used: %d' % (bCount))

DEBUG = sys.argv[2]
inspectDisk(sys.argv[1])
