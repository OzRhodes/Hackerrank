
#countingValleys.py
def countingValleys(n, s):
    hike_level = 0
    valleycount = 0
    at_sea_level = True
    in_valley = False
    for change in range(len(s)):
        if s[change] == 'U':
            hike_level += 1
                    
        if s[change] == 'D':
            hike_level -= 1
            
        if hike_level == 0:
            at_sea_level = True
        else:
            at_sea_level = False
        
        if s[change] == 'U' and at_sea_level:
            valleycount += 1
    return valleycount
            
            
    
    
    
    
s = 'UDDDUDUU'
n = len(s)
print (countingValleys(n,s))