import decimal
import json
import random
import threading
from time import sleep
import sys
from colourterm import tform
from industrialobjects import *

def get_config(filename):
    try:
        with open(filename, 'r') as infile:
            return json.load(infile)
    except:
        print("\r"+tform("Incorrect configuration file.", "FAIL"))
        print("System configuration must be JSON format")
        sys.exit()

def makeStuff(d):
    system = control_system()

    for key, value in d.items():
        print(key)
        s = d[key]
        for key, value in s.items():
            print(" - " + key)
            current = key
            si = s[key]
            for l in si:
                print("   - " + l["label"])

config = str(sys.argv[1])
sysconf = get_config(config)

makeStuff(sysconf)