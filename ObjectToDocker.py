import decimal
import json
import random
import threading
from time import sleep
import sys
from colourterm import tform
from industrialobjects import *

#==============================================================================

def get_config(filename):
    try:
        with open(filename, 'r') as infile:
            return json.load(infile)
    except:
        print("\r"+tform("Incorrect configuration file.", "FAIL"))
        print("System configuration must be JSON format")
        sys.exit()

#------------------------------------------------------------------------------

def store_config(filename, config):
    with open(filename, 'w') as outfile:
        outfile.write(config)

#------------------------------------------------------------------------------

def store_log(filename, log):
    with open(filename, 'w') as outfile:
        for line in log:
            outfile.write(line+'\n')

#------------------------------------------------------------------------------

def startup(config):
    print(tform("Starting program",'HEADER'))

    print("Fetching configuration")
    sysconf = get_config(config)
    #print(json.dumps(sysconf, indent=2, sort_keys=True))

    print(tform("Program running",'OKGREEN'))

    return sysconf

#------------------------------------------------------------------------------

def shutdown(logs):
    print(tform("Halting program",'WARNING'))

    store_log('tank_sim.log', logs)

    print(tform("Program ended", 'OKGREEN'))

#------------------------------------------------------------------------------

def JSON2Obj(d):
    print(tform("Building control system",'HEADER'))
    system = control_system()

    for key, value in d.items():
        s = d[key]
        for key, value in s.items():
            current = key
            si = s[key]
            for l in si:
                if current == "objects":
                    system.addObject(industial_object(l["label"], l["value"]))
                if current == "sensors":
                    obj = system.getObject(l["object"])
                    system.addSensor(industrial_sensor(obj, l["label"]))
                if current == "actuators":
                    pass
                if current == "plcs":
                    pass

    return system

#------------------------------------------------------------------------------

def main():
    if(len(sys.argv) < 3):
        print("\r"+tform("Incorrect usage.", "FAIL"))
        print("eg: sim.py <system_configuration> <output_directory>")
        sys.exit()

    config = str(sys.argv[1])
    cycles = str(sys.argv[2])

    sysconf = startup(config)

    system = JSON2Obj(sysconf)

    shutdown("no logs")

#------------------------------------------------------------------------------

main()

#------------------------------------------------------------------------------
