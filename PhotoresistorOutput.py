from MCP3008 import MCP3008

for i in range(10):
     adc = MCP3008()
     print("Photoresistor 1 value: ", adc.read1(channel=0)) # if necesarry perform several times

for i in range(10):
     adc = MCP3008()
     print("Photoresistor 2 value: ", adc.read2(channel=1)) # if necesarry perform several times

for i in range(10):
     adc = MCP3008()
     print("Photoresistor 3 value: ", adc.read3(channel=2)) # if necesarry perform several times

for i in range(10):
     adc = MCP3008()
     print("Photoresistor 4 value: ", adc.read4(channel=3)) # if necesarry perform several times

#from webiopi.devices.analog import MCP3008
#adc = MCP3008()
#print("Read 1:", adc.analogRead(0))
#print("Read 2:", adc.analogRead(1))
