#drawingbook.py


import math

def pageCount(n, p):
    # 
    # 10 of 100 -->  n/2 = 5
    # 20 of 100 -->  n/2 = 10
    # 90 of 100 -->  (n-p*1)/2 = 5
    # if p == 1 or p == n:
    #    no turns
    # if the page is > half n then start at the back
    # else start at the front
    
    if (p == 1 or p == n):
        return 0
    
    if p > (n/2):
        if p%2 == 0:
            result = int((n-p)//2)
        else:
            result = int((n-p+1)//2)
        return result
    else:
        result = int(p/2)
        return result

n = 12
p = 5


print (pageCount(n,p))
