#organizingContainers.py

def organizingContainers(container):
    
    n = len(container[0])

    container_max=[]   # max number of balls in a a container is set
    ball_type=[]       # number of balls of each type
    
    #size of containers
    for ball in range(n): 
        balls_in_container = sum(container[ball])
        container_max.append(balls_in_container)
    #number of each ball type
    ball_count = 0
    for col in range(n):
        for row in range(n):
            ball_count += container[row][col]

        ball_type.append(ball_count)
        ball_count=0
    container_max = sorted(container_max)
    ball_type = sorted(ball_type)
    for check in range(n):
        if container_max[check]!=ball_type[check]:
            return 'Impossible'
    return 'Possible'    
            
        

container = [[0,2,1], [1,1,1], [2,0,0]]

print(organizingContainers(container))

