#absolutePermutation.py


def absolutePermutation(n, k):
    result = []
    sub_list = []
    if k == 0:
        for i in range(1,n+1):
            result.append(i)
        return result
    if n%(2*k) !=0:
        result.append(-1)
        return result
    num = 0
    while num < n//(2*k):
        
        for i in range(0,2*k):
            sub_list.append((i+1)+k*2*num)
        for perm in range(len(sub_list)):
            if perm < (len(sub_list)+1) // 2:
                result.append(sub_list[perm+(len(sub_list)) // 2])
            else:
                result.append(sub_list[perm-((len(sub_list))) // 2])
        num += 1
        sub_list = []
    return result
    


n = 3
k = 0
print(absolutePermutation(n, k))

