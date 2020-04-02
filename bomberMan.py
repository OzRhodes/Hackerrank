#bomberMan.py



def detonation(grid, n_r, n_c):   # it returns grid as a list of lists
    new_above = ''
    new_current_row =''
    new_below = ''
    new_row = ''
    grid2= []
    
    # single row
    if n_r ==1:
        for j in range(len(grid[0])):
            if j == len(grid[0])-1:
                if grid[0][j] == 'O' or grid[0][j-1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'
            elif j == 0:
                if grid[0][j] == 'O' or grid[0][j+1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'
            else:                
                if grid[0][j] == 'O' or grid[0][j+1] == 'O' or grid[0][j-1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'
        grid2.append(new_row)
        new_row = ''
        return grid2


    # single col
    if n_c ==1:
        for j in range(len(grid)):
            if j == len(grid)-1:
                if grid[j-1][0] == 'O' or grid[j][0] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'
                grid2.append(new_row)
                new_row = ''
            elif j == 0:
                if grid[j][0] == 'O' or grid[j+1][0] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'
                grid2.append(new_row)
                new_row = ''        
            else:                
                if grid[j][0] == 'O' or grid[j+1][0] == 'O' or grid[j-1][0] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'
                grid2.append(new_row)
                new_row = ''

        return grid2



    for i in range(len(grid)):
        for j in range(len(grid[i])):

            #check top right
            if i == 0 and j == len(grid[i])-1:     
                if grid[i][j] == 'O' or grid[i+1][j] == 'O' or grid[i][j-1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'

            #check top left
            elif i == 0 and j == 0:     
                if grid[i][j] == 'O' or grid[i+1][j] == 'O' or grid[i][j+1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'

            #check bottom left
            elif i == len(grid)-1 and j == 0:     
                if grid[i][j] == 'O' or grid[i-1][j] == 'O' or grid[i][j+1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'
            #check bottom right
            elif i == len(grid)-1 and j == len(grid[i])-1:     
                if grid[i][j] == 'O' or grid[i-1][j] == 'O' or grid[i][j-1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'
                
            #top row
            elif i == 0 and j != len(grid[i])-1 and j != 0:    

                if grid[i][j] == 'O' or grid[i][j+1] == 'O' or grid[i+1][j] == 'O' or grid[i][j-1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'            
            # bottom row
            elif i == len(grid)-1 and j != len(grid[i])-1 and j != 0: 
                if grid[i][j] == 'O' or grid[i-1][j] == 'O' or grid[i][j-1] == 'O' or grid[i][j+1] =='O':
                    new_row += '.'
                else:
                    new_row += 'O'            
            #left col
            elif j == 0 and i != len(grid)-1 and i != 0:
                if grid[i][j] == 'O' or grid[i-1][j] == 'O' or grid[i+1][j] == 'O' or grid[i][j+1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'            
            #  right col
            elif j == len(grid[i])-1 and i != len(grid)-1 and i != 0:
                if grid[i][j] == 'O' or grid[i-1][j] == 'O' or grid[i+1][j] == 'O' or grid[i][j-1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'                
                
             #          anywhere else
            else:    
                if grid[i][j] == 'O' or grid[i+1][j] == 'O' or grid[i][j+1] == 'O' or grid[i-1][j] == 'O' or grid[i][j-1] == 'O':
                    new_row += '.'
                else:
                    new_row += 'O'   
                
        grid2.append(new_row)
        new_row = ''
    return grid2

def bomberMan(n, grid):
        n_r = len(grid)
        n_c = len(grid[0])
        
        if n == 1: return grid
        
        elif n % 2 == 0: return ['O'*n_c]*n_r  # every 2 seconds the grid is filled
        elif n % 4 == 3: return detonation(grid, n_r, n_c)
        elif n % 4 == 1: return detonation(detonation(grid, n_r, n_c), n_r, n_c)

n = 3
grid = ['.......','...O...','....O..','.......','OO.....','OO.....']

print(bomberMan(n, grid))






