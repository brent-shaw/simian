import decimal
import json
import random
import threading
from time import sleep
import sys
from colourterm import tform
from industrialobjects import *

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

#------------------------------------------------------------------------------

temp = 30.0

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

def noFaults(a):
    for o in a:
        if (o.fault):
            return False
    return True

#------------------------------------------------------------------------------

def runSimulation(system, cycles):
    cycleCount = 0
    while(noFaults(system.objects)):
        updates = system.update()

        report = system.reportTanks(cycleCount)
        if updates[0]:
            yield updates[1]
        yield report

        cycleCount += 1
        #sleep(0.01)
        if cycleCount == cycles:
            break

    report = system.reportTanks(None)
    yield report

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

def main():
    if(len(sys.argv) < 3):
        print("\r"+tform("Incorrect usage.", "FAIL"))
        print("eg: sim.py <system_configuration> <simulated_cycles>")
        sys.exit()

    config = str(sys.argv[1])
    cycles = int(sys.argv[2])

    sysconf = startup(config)

    system = JSON2Obj(sysconf)

    try:
        print("Running simulation for "+str(cycles)+" cycles.")
        logs = runSimulation(system, cycles)
        print(tform("Simulation completed successfully", 'OKGREEN'))
    except(KeyboardInterrupt):
        print("\r"+tform("Simultaion interrupted by user", "FAIL"))

    shutdown(logs)

#------------------------------------------------------------------------------

main()

#------------------------------------------------------------------------------
