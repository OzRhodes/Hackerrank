#kaprekarNumbers.py

def kaprekarNumbers(p, q):
    valid_range = False
    results = []
    for i in range(p,q+1):
        if i == 1:
            results.append(i)
            valid_range = True
        else:
            d=str(i)
            num = i*i
            if num > 10:
                num=str(num)
                first = int(num[0:(len(num)-len(d))])
                second = int(num[len(num)-len(d):])
                if first + second == i:
                    results.append(i)
                    valid_range = True
                
    if valid_range == False:
        print('INVALID RANGE')       
    for num in results:
        print(num, end = ' ')     
            
p = 1
q = 100
kaprekarNumbers(p, q)