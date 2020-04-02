#howManyGames.py

# p initial price
# d decrememt
# m minimum price
# s wallet amount

def howManyGames(p, d, m, s):
    count = 0
    price = p 

    while s>= price:
        count += 1
        s -= price
        if price - d >= m:
            price -=d 
        else:
            price =m

    return count

p = 20
d = 3
m = 6
s = 80

print (howManyGames(p, d, m, s))

