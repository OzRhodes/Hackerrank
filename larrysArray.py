#larrysArray.py


def larrysArray(A):
    # if the sum of the inversions (lower number immediately after a 
    # higher one is %2 = 0 then NO else YES
    # eg (2,3,1) - 1 inversion therefore %1 = 1 therefore Yes
    # eg (3,2,1) - 2 inversions therefore %2 = 0 therefore No
    
    if sum([1 for i in range(len(A)) for j in range(i+1, len(A)) if A[i] > A[j] ])%2:
        return 'NO' 
    else: 
        return "YES"
    
A = [3,2,1,4,5]
print(larrysArray(A))