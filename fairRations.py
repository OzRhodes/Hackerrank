#fairRations.py

def fairRations(B):
    donate=0
    
    
    if sum(B) % 2 != 0:
        return 'NO'
    
    index = len(B)
    while index>0:
        if B[index-1]%2 != 0:
            donate +=2
            B[index-2] += 1
        index -=1
    
    return donate





B = [2,3,4,5,6]
print(fairRations(B))


