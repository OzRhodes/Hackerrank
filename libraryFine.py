#libraryFine.py

def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0

    if d1 == d2 and m1 == m2 and y1 == y2:
            return fine
    if y1<y2:
        return fine
    if y1==y2 and m1<m2:
        return fine
    if m1==m2 and y1==y2 and d2>d1:
        return fine 
    elif y1 > y2:
        fine = (y1 - y2) * 10000
        return fine
    elif m1 > m2:
       fine = (m1 - m2) * 500
       return fine
    elif d1 > d2:
        fine = (d1-d2)*15
        return fine
   

    

d1,m1,y1 = 9,6,2015
d2,m2,y2 = 6,6,2015


print (libraryFine(d1, m1, y1, d2, m2, y2))




 