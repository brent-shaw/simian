import random
from colourterm import tform

#==============================================================================

class industial_object():
    def __init__(self, label, v=0, l=0, t=0, d=1):
        print("  Initialised industial_object")
        self.label = label
        self.capacity = v
        self.value = v
        self.limit = l
        self.trend = t
        self.default = d
        self.fault = False

    def setValue(self, v):
        self.value = v
        if (self.trend == 0):
            if (self.value <= self.limit):
                self.fault = True
        else:
            if (self.value >= self.limit):
                self.fault = True

    def inc(self, v):
        self.value += v
        if (self.trend == 0):
            if (self.value <= self.limit):
                self.fault = True
        else:
            if (self.value >= self.limit):
                self.fault = True

    def dec(self, v):
        self.value -= v
        if (self.trend == 0):
            if (self.value <= self.limit):
                self.fault = True
        else:
            if (self.value >= self.limit):
                self.fault = True

    def update(self):
        if (self.trend == 0):
            self.dec(self.default+(random.randint(0,10)/10))
        else:
            self.inc(self.default+(random.randint(0,10)/10))

#==============================================================================

class industrial_sensor():

    def __init__(self, o, l):
        self.source = o
        self.label = l
        print("  Initialised sensor")

    def read(self):
        return self.source.value


#==============================================================================

class actuator():

    def __init__(self):
        print("  Initialised actuator")

#==============================================================================

class rtu():

    def __init__(self):
        print("  Initialised rtu")

#==============================================================================

class plc():

    def __init__(self):
        print("  Initialised plc")

#==============================================================================

class control_system():
    def __init__(self):
        self.objects = []
        self.sensors = []
        self.actuators = []
        self.plcs = []
        self.rtus = []
        print("  Initialised control_system")

    def addObject(self, o):
        self.objects.append(o)

    def addSensor(self, o):
        self.sensors.append(o)

    def addPLC(self, o):
        self.plcs.append(o)

    def getObject(self, l):
        for o in self.objects:
            if o.label == l:
                return o

    def update(self):
        update = ["SYSTEM UPDATE"]
        updated = False
        formatter = "{: <15}"
        for sensor in self.sensors:
            sensor.source.update()
            if (sensor.read() < (sensor.source.capacity*0.3)):
                sensor.source.inc((random.randint(0,100)+(random.randint(0,100))))
                update.append("> "+tform("LEVEL: Adding water",'OKBLUE')+(" "*4))
                updated = True
            else:
                update.append(">")
            formatter += " {: <25}"
        return (updated, formatter.format(*update))


    def reportTanks(self, cycle):
        if cycle == None:
            output = ["END CONDITIONS"]
        else:
            output = ["Cycle: "+str(cycle)]
        for o in self.objects:
            if (o.fault):
                output.append("> "+tform("FAULT: Tank is dry",'FAIL')+(" "*8))
            else:
                if o.value <= (o.capacity*0.35):
                    output.append("> "+tform("tank level: {0:.2f}".format(o.value),'WARNING')+(" "*5))
                else:
                    output.append("> tank level: {0:.2f}".format(o.value))
        return "{: <15} {: <25} {: <25} {: <25} {: <25} {: <25}".format(*output)

