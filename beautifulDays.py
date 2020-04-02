#beautifulDays.py


def beautifulDays(i, j, k):
# get list of days
# get inverse numbers
# if (day x - inv day x) $k is zero
# its a beautiful day
# 
    beautiful_days = 0
    days = []
    rev_days = []
    for day in range (i,j+1):
        days.append(day)
# reverse the numbers
    for day in range (len(days)):
        y=0
        number = days[day]
        while(number >= 1):
            z = number % 10
            y = 10 * y + z
            number = number / 10
            number = int(number)
        rev_days.append(y)
    
    for day in range (len(days)):
        if abs((days[day]-rev_days[day])%k) == 0:
            beautiful_days += 1
    return beautiful_days

i = 20
j = 23
k = 6
print (beautifulDays(i, j, k))