#jumpingOnClouds.py
# energy
# -1 jump
# -2 if cloud == 1

def jumpingOnClouds(c, k):
    posn = 0
    energy = 100
    end = False
    while end != True and energy >1:
        # jump
        posn += k
        posn = posn%len(c)
        if posn == 0:
            end = True
        energy -=1
        if c[posn]==1:
            energy -=2
    return energy    
            
    
k = 2
c = [0,0,1,0,0,1,1,0]
print (jumpingOnClouds(c, k))

