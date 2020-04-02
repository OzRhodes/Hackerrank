#pickingNumbers.py

def pickingNumbers(a):
    a.sort()
    b = []
    count = 0
    for num in range (0,100):
        b.append(a.count(num))
    count = max(b)
    for num in range(len(b)-1):
        if (b[num] and b[num+1] ) > 0:
            if  b[num]+b[num+1] > count: 
                count = b[num]+b[num+1]
    return count

a = [4,97,5,97,97,4,97,4,97,97,97,97,4,4,5,5,97,5,97,99,4,97,5,97,97,97,5,5,97,4,5,97,97,5,97,4,97,5,4,4,97,5,5,5,4,97,97,4,97,5,4,4,97,97,97,5,5,97,4,97,97,5,4,97,97,4,97,97,97,5,4,4,97,4,4,97,5,97,97,97,97,4,97,5,97,5,4,97,4,5,97,97,5,97,5,97,5,97,97,97]
print (pickingNumbers(a))