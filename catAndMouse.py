#catAndMouse(x, y, z)

def catAndMouse(x, y, z):
    
    catA = abs(x-z)
    catB = abs(y-z)
    
    if catA > catB:
        return 'Cat B'
    if catA == catB:
        return 'Mouse C'
    else:
        return 'Cat A'




x = 1
y = 3
z = 2
print (catAndMouse(x, y, z))