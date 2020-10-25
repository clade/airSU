# This file is executed on every boot (including wake-boot from deepsleep)
import sys
sys.path[1] = '/flash/lib'

import uos

from m5stack import lcd
#lcd.tft_writecmd(0x21) # for M5 grey only
logo = "/flash/images/physique_SU.jpg"
lcd.image(0, 0, logo)



## Mount sd card
uos.sdconfig(uos.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=4)
try:
    uos.mountsd()
    with_sd = True
except OSError:
    with_sd = False

## Real time clock
from machine import I2C, Pin
i2c = I2C(-1, scl=Pin(5, Pin.PULL_FLOAT), sda=Pin(2, Pin.PULL_FLOAT))
if 104 in i2c.scan():
    import ds3231_port
    from machine import RTC
    ds3231 = ds3231_port.DS3231(i2c)
    _ = ds3231.get_time()
    RTC().init(_)
    with_ds3231 = True    
else:
    with_ds3231 = False



