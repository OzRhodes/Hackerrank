#taumBday.py
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b   number of b 
#  2. INTEGER w   number of w
#  3. INTEGER bc  cost of b
#  4. INTEGER wc  cost of w
#  5. INTEGER z   cost of conversion


def taumBday(b, w, bc, wc, z):
    result = 0
    # Write your code here
    
    # no merit in changing
    if bc == wc :
        result = (b*bc) + (w*wc)
        return result
    
    if ((bc+z)>= wc) and ((wc+z)>=bc):
        result = (b*bc) + (w*wc)
        return result
    
    if bc > wc+z:
       result = ((b+w)*wc)+b*z
       return result
   
    if wc > bc+z:
       result = ((b+w)*bc)+w*z
       return result
   
        

b = 7
w = 7
bc = 4
wc = 2
z = 1

print (taumBday(b, w, bc, wc, z))

