#minimumDistances.py


def minimumDistances(a):
    min_dist = 0
    
    dist =[]
    for i in range (len(a)-1):
        if a[i] in a[i+1:]:
            test = a[i]
            test2 = a[i+1:].index(a[i])+i
            correction = len(a) - len(a[i+1:])
            min_dist = a[i+1:].index(a[i]) - i + correction
            dist.append(min_dist)
    if len(dist) > 0:
        result  = min(dist)
    else:
        result = -1
    return result
    

a = [7,4,3,1,3,4,7]
print (minimumDistances(a))