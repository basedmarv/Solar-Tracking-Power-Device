from spidev import SpiDev

class MCP3008:
     def __init__(self, bus=0, device = 0):
          self.bus, self.device = bus, device
          self.spi=SpiDev()
          self.open()
          self.spi.max_speed_hz = 1000000 # 1MHz

     def open(self):
          self.spi.open(self.bus, self.device)
          self.spi.max_speed_hz = 1000000 # 1MHz

     def read1(self, channel = 0):
          adc = self.spi.xfer2([1,(8+channel) << 4, 0])
          data = ((adc[1] & 3) << 8) + adc[2]     
          return data

     def read2(self, channel = 1):
          adc = self.spi.xfer2([1,(8+channel) << 4, 0])
          data = ((adc[1] & 3) << 8) + adc[2]     
          return data

     def read3(self, channel = 2):
          adc = self.spi.xfer2([1,(8+channel) << 4, 0])
          data = ((adc[1] & 3) << 8) + adc[2]     
          return data
     
     def read4(self, channel = 3):
          adc = self.spi.xfer2([1,(8+channel) << 4, 0])
          data = ((adc[1] & 3) << 8) + adc[2]     
          return data
	 #Solar read 
     def read5(self, channel = 4):
          adc = self.spi.xfer2([1,(8+channel) << 4, 0])
          data = ((adc[1] & 3) << 8) + adc[2]     
          return data
	 #Battery read	  
     def read6(self, channel = 5):
          adc = self.spi.xfer2([1,(8+channel) << 4, 0])
          data = ((adc[1] & 3) << 8) + adc[2]     
          return data

     def close(self):
          self.spi.close()
