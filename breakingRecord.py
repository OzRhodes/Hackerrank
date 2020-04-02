import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    lowest = 0
    highest = 0
    high_change =0
    low_change = 0
    
    lowest =scores[0]
    highest = scores[0]
    
    for num in range (1,len(scores)):
        if scores[num] > highest:
            highest = scores[num]
            high_change += 1
        if  scores[num] < lowest:
            lowest = scores[num]
            low_change += 1
     
    return high_change, low_change  

scores = [3,4,21,36,10,28,35,2,24,42]
print (breakingRecords(scores))
    