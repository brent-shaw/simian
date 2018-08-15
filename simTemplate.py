#from pymodbus.client.sync import ModbusTcpClient as ModbusClient
import threading
import random
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

#client = ModbusClient('172.20.0.2', port=502)
#client.connect()
#print('ModbusClient started')
#rr = client.read_coils(1, 1, unit=0x02)

cycleCount = {{cycleCount}}
tank = {{tankSize}}

def printit():
    global tank
    threading.Timer(0.01, printit).start()
    tmp = random.randint(0,10)
    #print(tmp)
    if tank < 333:
        tank += random.randint(0,100)+(random.randint(0,100))
        print(str(tank))
        #rq = client.write_coils(1, [True]*8)
        #rr = client.read_coils(1,8)
    else:
        tank -= 1+(random.randint(0,10)/10)
        print(str(tank))
        #rq = client.write_coils(1, [False]*8)
        #rr = client.read_coils(1,8)

printit()

#client.close()
