#surfaceArea.py

def surfaceArea(A):
    area = 0
    for i in range(len(A)):                 # for list in list.
        for e in range(len(A[i])):          # for element in list
            c = A[i][e]                     # current cell val
            s = (c*4)+2                     # surface for the current cell
            
            if i > 0:                       #side limit
                s -= min(c,A[i-1][e])*2     # remove the area of the smallest side
            if e > 0:                       #upper limit
                s -= min(c,A[i][e-1])*2     # remove the area of the smallest front
                
            area += s
            
    return area 

A = [[1, 3, 4],[2, 2, 3],[1,2,4]]

print(surfaceArea(A))