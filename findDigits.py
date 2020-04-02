#findDigits.py


def findDigits(n):
    numbers = list(map(int, str(n)))
    divisors = 0
    for num in range (len(numbers)):
        if numbers[num] != 0:
            if n % numbers[num] ==0:
                divisors += 1
    return divisors

n = 123
print (findDigits(n))
