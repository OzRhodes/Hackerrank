import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    count = 0
    sum = 0
    # contiguous block of d with a sum of m on the bricks
    if m == 1:
       if s[0] == d:
           count = 1
    else:
        for itr in range (len(s) - m + 1):
            for brick in range(itr, itr + m):
                sum += s[brick]
            if sum == d:
                count += 1
            sum = 0    
    
    return (count)
#s=[2,5,1,3,4,4,3,5,1,1,2,1,4,1,3,3,4,2,1]
s = [1,2,1,3,2]
#d = 18
d = 3
#m = 7
m = 2
    
print (birthday(s,d,m))