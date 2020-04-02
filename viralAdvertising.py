#viralAdvertising.py
import math

def viralAdvertising(n):
    
    
    shared = 5
    liked = 0
    cumulative = 0

    for day in range(n):
        liked = math.floor(shared/2)
        shared = liked * 3
        cumulative += liked
        
        
        
        
        

n = 5
viralAdvertising(n)