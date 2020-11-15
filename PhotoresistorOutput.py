from MCP3008 import MCP3008

for i in range(100):
     adc = MCP3008()
     print(adc.read(channel=0)) # if necesarry perform several times
