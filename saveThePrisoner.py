#saveThePrisoner.py


def saveThePrisoner(n, m, s):
    r = m % n
    seat = r+s-1
    if seat % n == 0:
        return n
    else:
        return seat % n

n = 7
m = 19
s = 2


print (saveThePrisoner(n, m, s))


