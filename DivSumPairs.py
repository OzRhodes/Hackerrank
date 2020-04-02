#DivSumPairs

import itertools
import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for x in itertools.permutations(ar,2):
        if (x[0] + x[1])%k == 0:
            count += 1
            
    return int(count/2)



ar =[1,3,2,6,1,2]
k = 3
n = 6
print (divisibleSumPairs(n, k, ar))