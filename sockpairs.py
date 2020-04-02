#sockpairs.py

def sockMerchant(n, ar):
    set_ar = []
    pair = []
    for item in range (len(ar)):
        if ar[item] not in set_ar:
            set_ar.append(ar[item])
            
    for socktype in range (len(set_ar)):
        if set_ar[socktype] in ar:
            count = ar.count(set_ar[socktype])
            pair.append(count)
    
    
    for socktype in range (len(pair)):
        pair[socktype] = int(pair[socktype] / 2)
    return sum(pair)     
    
    
n = 9
ar = [10,20,20,10,10,30,50,10,20]
print(sockMerchant(n, ar))