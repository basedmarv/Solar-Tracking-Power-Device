#Main author: Amber from kookyeye.com
#Modified for this project by: Marvin Neil Sabas & Michael Sanchez-Hernandez

import RPi.GPIO as GPIO
import time

AO_pin = 4 #channel pin 4
A1_pin = 5 #channel pin 4
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

#Initialize GPIO 
def init():
     GPIO.setwarnings(False)
     GPIO.setmode(GPIO.BCM)
     # Set up the SPI interface pins
     GPIO.setup(SPIMOSI, GPIO.OUT) 
     GPIO.setup(SPIMISO, GPIO.IN)
     GPIO.setup(SPICLK, GPIO.OUT)
     GPIO.setup(SPICS, GPIO.OUT)
     pass

#read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
     #Check if reading outside ADC pins 
     if ((adcnum > 7) or (adcnum < 0)):
          return -1
     
     GPIO.output(cspin, True)  
     GPIO.output(clockpin, False)  # start clock low
     GPIO.output(cspin, False)     # bring CS low

     commandout = adcnum
     commandout |= 0x18  # start bit + single-ended bit
     commandout <<= 3    # we only need to send 5 bits here
     
     for i in range(5):
          if (commandout & 0x80):
               GPIO.output(mosipin, True)
          else:
               GPIO.output(mosipin, False)
          commandout <<= 1
          GPIO.output(clockpin, True)
          GPIO.output(clockpin, False)
     adcout = 0

     # read in one empty bit, one null bit and 10 ADC bits
     for i in range(12):
          GPIO.output(clockpin, True)
          GPIO.output(clockpin, False)
          adcout <<= 1
          if (GPIO.input(misopin)):
               adcout |= 0x1

     GPIO.output(cspin, True)
     adcout >>= 1       # first bit is 'null' so drop it
     return adcout

def main():
     init()
     time.sleep(1)
     while True:
          ad_value = readadc(AO_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
          solarVoltage= ad_value*(3.3/1024)*5
          print(f'Solar voltage: {solarVoltage}.')
          #time.sleep(1) 
          ad_value = readadc(A1_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
          batteryVoltage= ad_value*(3.3/1024)*5
          print(f'Battery voltage: {batteryVoltage}.')
          time.sleep(1)
                  
if __name__ =='__main__':
     try:
          main()
     except KeyboardInterrupt:
          pass
     GPIO.cleanup() 
          
          
