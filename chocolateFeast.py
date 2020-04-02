#chocolateFeast.py

def chocolateFeast(n, c, m):
    result = 0
    bars = int(n/c)
    result += bars
    wrappers = bars
    while wrappers >= m:
        bars = int(wrappers / m)
        wrappers = wrappers % m
        wrappers += bars
        result += bars
    return result
n = 10
c = 2
m = 5

print (chocolateFeast(n, c, m))
