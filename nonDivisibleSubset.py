
#nonDivisibleSubset.py 

def nonDivisibleSubset(k, s):
    #k = int
    # s = array
    
    d = {x:[] for x in range(k)}

    for i in range(len(s)): 
        d[s[i]%k].append(s[i])
    count = 0
    if len(d[0]) > 0:
        count = 1
    the_set = set([(x,k-x) for x in range(1,k//2+1)])
    for i,j in the_set:
        if i != j:
            if len(d[i]) > len(d[j]):
                count += len(d[i])
            else:
                count += len(d[j])
        else:
            if len(d[i]) > 0:
                count += 1
    return count


s=[1,2,7,4]
k = 3
print(nonDivisibleSubset(k, s))