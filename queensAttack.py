#queensAttack.py



# n: square
# k: an integer, the number of obstacles on the board
# r_q: integer, the row number of the queen's position
# c_q: integer, the column number of the queen's position
# obstacles: a two dimensional array of integers where each element is an array of integers, the row and column of an obstacle

def queensAttack(n, k, r_q, c_q, obstacles):
    
    # if no obs, find the queen attack squares to the closest edge 
    up = n-r_q
    down = r_q-1
    left = c_q-1
    right = n-c_q

    upleft = left if left < up else up
    upright = right if right < up else up
    dnleft = left if left < down else down
    dnright =right if right < down else down
    
    #run through the obstacles
    # if the obstacle is in line  ie, row or column is same as queen of row and column are in y=x
    # reset the number of squares avaiable to the queen
    
    for obstacle in range(len(obstacles)):
        
        row = obstacles[obstacle][0]
        col = obstacles[obstacle][1]  
        
        if col == c_q:
            if row > r_q: 
                if row-r_q -1 < up:
                    up = row-r_q-1
            elif row < r_q: 
                if r_q-row-1 <  down:
                    down = r_q-row-1
        
        if row == r_q:
            if col < c_q:  
                if c_q - col-1 < left:
                    left = c_q - col -1
            elif col > c_q:
                if col-c_q -1< right:
                    right = col-c_q -1
        
        #check diags
        #upright
        if row > r_q and col > c_q: 
            if col-c_q == row-r_q:
                if row-r_q-1 < upright:
                    upright = row-r_q-1
        #upleft
        if row > r_q and col < c_q: 
            if c_q-col == row-r_q:
                 if row-r_q-1< upleft:
                    upleft = row-r_q-1
        #downright       
        if col > c_q and row < r_q: 
                if r_q-row == col-c_q:
                    if r_q-row-1 < dnright:
                        dnright = r_q-row-1
        #downleft
        if col < c_q and row < r_q:  
                if r_q-row == c_q-col:
                    if r_q-row-1 < dnleft:
                        dnleft= r_q-row-1
                    
    count = (upleft)+(up)+(upright)+(right)+(dnright)+(down)+(dnleft)+(left)

    return count 


n = 5
k = 3
r_q = 3
c_q = 3
obstacles =[(5,1),(5,3),(5,5),(3,5),(1,5),(1,3),(1,1),(3,1)]

print(queensAttack(n, k, r_q, c_q, obstacles))


