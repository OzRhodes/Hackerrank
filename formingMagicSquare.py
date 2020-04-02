#formingMagicSquare.py


#magic square magic sum is n(n**2+1)/2
# for n = 3 this us 15
# 1 goes at n/2, n-1
# i-1, j+1 
# if i= -1 --> i = n-1
# if j = n, j = 0
# if position is occupied i = i + 1, j = j - 2
# if -1, n --> 0, n-2

possible_squares = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]

def formingMagicSquare(s):
    cost = []
    for square in range (8):
        squarecost = 0
        for i in range(3):
            for j in range(3):
                value = abs(s[i][j]-possible_squares[square][i][j])
                squarecost += value
        cost.append(squarecost)
    return min(cost)        
        
        

s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]

print (formingMagicSquare(s))