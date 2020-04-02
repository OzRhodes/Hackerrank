#permutationEquation.py



def permutationEquation(p):
    results=[]
    for x in range(len(p)):
        ind1 = p.index(x+1)
        result = p.index(ind1+1)
        results.append(result+1)
    return results
    



p=[5,2,1,3,4]

print (permutationEquation(p))

42513

