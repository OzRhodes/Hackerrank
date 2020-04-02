#dayofprogrammer.py

#1700-2700 inclusive
#256 day
#1919 gregorian calendar
# in 1918 32 day of the year was 14 feb
# gregorian calendar 
#leap year s divisible by 4 or 400 
# julian just by 4 
# given year y
# find the 256 day of that year
# print dd.mm.yyyy
#
# gregorian calendar 13 Sep
# gregorian leap 12 Sep
# Julian
#
#

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leap1 = year % 4
    leap2 = year % 400
    leap3 = year % 100
    date =''
    if year == 1918:
        return '26.09.1918'
    if year <1917 and leap1 ==0:
            date = '12.09.'+ str(year)
    elif (leap1 == 0 and leap3 != 0) or leap2 == 0:
        date = '12.09.'+str(year)
    else:
        date = '13.09.'+str(year)
    return date


year = 1918

print (dayOfProgrammer(year))
