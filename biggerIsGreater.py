
#biggerIsGreater.py

'''
Step 1: Find the largest index k, such that A[k] < A[k + 1]. 
        If not exist, this is the last permutation. (in this problem just reverse the vector and return.)
Step 2: Find the largest index l, such that A[l] > A[k] and l > k.
Step 3: Swap A[k] and A[l].
Step 4: Reverse A[k + 1] to the end.'''

def biggerIsGreater(w):
    if len(w) == 1:
        result = 'no answer'
        return result
        
    result=''
    result2 = ''
    index = 0
    pivot = -1
    if len(w)==1 or len(w)==0:
        result = 'no answer'
        return result
    if len(w)==2:
        if (w[1])>(w[0]):
            result = result + w[1] + w[0]
            return result
        else:
            result = 'no answer'
            return result
    
    index = len(w)-1
    while index > 0:
        
        if w[index]<=w[index-1]:
            index -=1
        else:
            pivot = index-1
            break 

    if pivot==-1:
        result = 'no answer'
        return result     
        
    index = len(w)-1
   
    while index > 0:
        if w[index]<=w[pivot] or index<=pivot:
            index -=1
        else:
            break
        
    result = w[:pivot]
    result = result + w[index]
    
    result2 = w[pivot+1:index]
    
    #result2 = result2 + w[pivot+1:index-1]
    result2 = result2 + w[pivot]
    
    result2 = result2 + w[index + 1:]
    
    result2 = result2[::-1]
    result = result + result2
    
    return result


input_str =[]
output_str = []

with open ('input.txt','r') as fi, open ('output.txt','r') as fo:
    for line1 in fi:
        input_str.append(line1.strip('\n'))
    for line2 in fo:
        output_str.append(line2.strip('\n'))
        

w='biehzcmjckznhwrfgglverxsezxuqpj'
print(biggerIsGreater(w))



