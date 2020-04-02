#repeatedString.py


def repeatedString(s, n): 
    length = len(s)
    if length >= n:
        s=s[:n]
        count = s.count('a')
        return  count 
    sub_length = n%length
    count = s.count('a')
    count = count * (n//length)
    subs = s[:sub_length]
    count += subs.count('a')
    return int(count)

s='aba'
n=9
print (repeatedString(s, n))