#strangeCounter.py

def strangeCounter(t):
    
    rem = 3
    while t > rem:
        t = t-rem
        rem *= 2
    return (rem-t+1)


t = 13
print(strangeCounter(t))