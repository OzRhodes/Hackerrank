#hurdleRace.py

def hurdleRace(k, height):
    doses = 0
    max_height = max(height)
    doses = max_height-k
    if doses<0:
        doses = 0
    
    return doses

k = 4
height =[1,6,3,5,2]



print (hurdleRace(k, height))