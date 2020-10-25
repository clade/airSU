""" Function to create DATA file with incrementing number

Usage :
    filename = get_filename(directory='/sd')

This function returns a new file name

"""

import os
import re
import time


expr = re.compile('DAT_([0-9][0-9][0-9][0-9]).txt')
filetemplate = "DAT_{i:04d}.txt"

def get_max_number(directory="/sd"):
    i = -1
    for elm in os.listdir(directory):
        res = expr.match(elm)
        if res is not None:
            i = max(i, int(res.group(1)))
    return i+1

def get_file_name(base_directory="/sd", time_tpl=None):
    if time_tpl is None:
        time_tpl = time.localtime()
    directory = make_dir_from_day(time_tpl, base_directory)
    i = get_max_number(directory)
    return directory + "/" + filetemplate.format(i=i)

def make_dir_from_day(time_tpl, base_directory='/sd'):
    year = time_tpl[0]
    month = time_tpl[1]
    day = time_tpl[2]
    os.mkdir(base_directory + '/{year:04d}'.format(year=year))
    os.mkdir(base_directory + '/{year:04d}/{month:02d}'.format(year=year, month=month))
    path = base_directory + '/{year:04d}/{month:02d}/{day:02d}'.format(year=year, month=month, day=day)
    os.mkdir(path)
    return path

