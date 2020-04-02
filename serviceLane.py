#serviceLane.py

    
def serviceLane(n, cases):
    results = []
    for case in cases:
        entry = case[0]
        exit = case[1]+1
        minimum = min(width[entry:exit])
        results.append(minimum)
    return results
    


width = [2,3,1,2,3,2,3,3]
cases = [(0,3),(4,6)]

print(serviceLane(n, cases))