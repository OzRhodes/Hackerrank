#squares.py
import math

def squares(a, b):
    count = 0
    number = 0
    # find first Square Number
    for num in range(a,b+1):
        number =  math.sqrt(num)
        if number.is_integer():
            count += 1
            break
    at_b = False
    while not at_b:
        number += 1
        square = number**2
        if square <= b:
            count += 1
        else:
            at_b = True     
    
    return count
    


a = 3
b = 255
print (squares(a, b))