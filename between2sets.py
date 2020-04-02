import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b

def getTotalX(a, b):
    
    max_len = len(a) + len(b)
    factors_arraya=[]
    factors_arrayb=[]
    common =[]
    
    
    for itr in range(1,101):
        for num in range (len(a)):
            if  itr % a[num] == 0:
                factors_arraya.append(itr)
    
        
    
    # b is an array of ints
    # get the gcb for the first array which is the upper boundary of factors

    
    for itr in range(1,101):
        for num in range (len(b)):
            if b[num] % itr == 0:
                factors_arrayb.append(itr)
                
    full_list = factors_arraya + factors_arrayb
    
    for num in range (len(full_list)):
        if full_list.count(num) == max_len:
            common.append(num)
    
    return len(common)

x =[2,4]
y = [16,32,96]

print (getTotalX(x, y))


