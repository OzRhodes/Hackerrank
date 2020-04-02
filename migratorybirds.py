#migratorybirds.py

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    max_id = 0
    most_id = 0
    arr.sort()
    list = []
    max_id = max(arr)   # find the largest ID used
    for id in range (1, max_id+1):
        list.append(arr.count(id))    # count each occurence of an ID
    for first_max in range(len(list)):
        if list[first_max] > list[most_id]:
            most_id = first_max        # find the id most occuring
        

    #allow for list starting at o
    return (most_id+1)

arr =[1,4,4,4,5,3]

print (migratoryBirds(arr))