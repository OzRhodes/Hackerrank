#bonapetite.py

def bonAppetit(bill, k, b):
    items = len(bill)
    bill_sum = sum(bill)
    calc = (bill_sum - bill[k]) /2
    if b == calc:
        return  'Bon Appetit'
    else:
        amt = b - calc
        return amt
    
b = 12
k = 1
bill =[3,10,2,9]

print (bonAppetit(bill, k, b))
