from machine import Pin, I2C
import time
from lib.nau7802.nau7802 import NAU7802

class Weight:
    def __init__(self, sck, sda, numReads=10):
        # i2c = I2C(scl=Pin(sck), sda=Pin(sda))
        self.scale = NAU7802(i2c)
        if self.scale.begin():
            print('Wight ready')
        
    def getWeight(self):
        adc_value = self.scale.read_adc()
        print("ADC Value:", adc_value)
        time.sleep(1)
        return adc_value
        # value = self.hx711.read_average(times=self.numReads)
        # return value / self.tare
        
    
    def getTare(self):
        return self.tare
    
    def setTare(self):
        self.tare = self.tare(self.numReads)
        
        