#gridSearch.py
from re import finditer
# Note that finditer must be replaced with re.finditer in the hackerrank code editor

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def gridSearch(G, P):
    answer = 'NO'
    lst1 = []
    lst2 = []
    rowG = 0
    rowP = 0
    while rowG < len(G)-len(P) +1:
        iter = 0
        pattern =  '(?='+ P[rowP]+')'
        for match in finditer(pattern, G[rowG]):
            lst1.append(match.start())
        while len(lst1)>0:
            iter +=1
            if len(lst1)>0 and iter>= len(P):
                answer= 'YES'
                return answer
            pattern =  '(?='+ P[rowP+iter]+')'
            for match in finditer(pattern, G[rowG+iter]):
                lst2.append(match.start())
            lst1 = intersection(lst1,lst2)
            lst2 = []
        rowG+= 1

    return answer



G = ['111111111111111','111111111111111','111111011111111','111111111111111','111111111111111']
P = ['11111','11111','11110']
print(gridSearch(G, P))



    
