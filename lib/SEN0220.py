# Author : Pierre Cladé
""" Driver for the SEN0220 (MH-Z19) CO2 sensor on ESP32

Usage : 
    uart = UART(2, tx=17, rx=16)
    sensor = SEN0220(uart)
    sensor.concentration
"""

from machine import UART
from utime import sleep

READ_GAS_CONCENTATION = b'\xff\x01\x86\x00\x00\x00\x00\x00\x79'
CALIBRATE = b'\xff\x01\x87\x00\x00\x00\x00\x00\x78'

class SEN0220(object):
    def __init__(self, uart=None):
        if uart is None:
            uart = UART(2, tx=17, rx=16)
        uart.init(9600, bits=8, parity=None, stop=1)
        self.uart = uart
    
    def read_concentration(self):
        self.uart.write(READ_GAS_CONCENTATION)
        sleep(0.001)
        out = self.uart.read()
        if len(out)==0:
            return 0
        return out[2]*256 + out[3]        
    
    @property
    def concentration(self):
        return self.read_concentration()
        
    def calibrate(self):
        self.uart.write(CALIBRATE)        

