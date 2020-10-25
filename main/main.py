from time import sleep, time, strftime, localtime
import machine

from version import __version__

from m5stack import buttonA
from SEN0220 import SEN0220
from data_path import get_file_name

run_main = True

t0 = time()
lcd.print('Press button A to stop.', color=lcd.BLACK, transparent=True)
while run_main and time()<t0+2: 
    if buttonA.wasPressed():
        run_main=False
        lcd.print('stopped')
    sleep(.1)
    lcd.print('.')

if run_main:
    lcd.clear()
    uid = machine.unique_id()
    uid = ''.join([hex(elm)[2:] for elm in uid])


    header = """# title : MEASUREMENT OF CO2 CONCENTRATION
# sensor : SEN0220
# id : {uid}
# col : date, concentation in ppm
""".format(uid=uid)

    base_directory = '/sd' if with_sd else '/flash'

    filename = get_file_name(base_directory=base_directory)

    with open(filename, 'w') as fd:
        fd.write(header)


    lcd.font(lcd.FONT_Default, transparent=False)
    lcd.print(filename, 5, 5)

    sen = SEN0220()
    i = 0
    while True:
        c = sen.concentration
        lcd.font(lcd.FONT_DejaVu24)
        lcd.print("{:6d} ppm     ".format(c), lcd.CENTER, lcd.CENTER)
        time_str = strftime('%Y-%m-%dT%H:%M:%S', localtime())
        lcd.font(lcd.FONT_Default)
        lcd.print(time_str + '\r', 5, 20)
        if i>3:
            with open(filename, 'a') as fd:
                 fd.write('{} {:6d}\n'.format(time_str, c))
        print(c)
        fd.flush()
        sleep(1)
        i += 1
