#utopianTree.py

def utopianTree(n):
    height = 1
    
    for cycle in range(1, n+1):

        if cycle%2 != 0:
            height *=2
        elif cycle%2 ==0 and cycle !=0:
            height +=1
    
    return height

n = 4
print (utopianTree(n))