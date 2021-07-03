if __name__ == '__main__':
    n = int(input())
    arr = input()
    new_arr = arr.split()
    int_arr =[]
    for i in new_arr:
        int_arr.append(int(i))
    highest1 = highest2 = max(int_arr) 
    while highest2 == highest1:
        ind = int_arr.index(highest2)
        int_arr.pop(ind)
        highest2 = max(int_arr)
    
        
        
    print(highest2)
