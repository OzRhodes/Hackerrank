# Complete the climbingLeaderboard function below.

def binarysearch(alice, scores):
    old_mid_value = 0
    lower_bound = 0
    upper_bound = len(scores)-1

   
    while (lower_bound <= upper_bound):
        mid_value = lower_bound+(upper_bound-lower_bound)//2
        if scores[mid_value] == alice:
                return mid_value
        elif (scores[mid_value] < alice and alice < scores[mid_value-1]):
            return mid_value
        elif (scores[mid_value]> alice and alice >= scores[mid_value+1]):
            return mid_value+1
        elif scores[mid_value] < alice:
            upper_bound = mid_value -1
        elif scores[mid_value] > alice:
            lower_bound = mid_value + 1


    
    
def climbingLeaderboard(scores, alice):
    rank = []
    lower_bound = 0
    upper_bound = 0
    mid_value = 0
    position = 1
    positions = []
    rank.append(1)
    
    for num in range(1, len(scores)):
        if scores[num] == scores[num-1]:
            rank.append(rank[num-1])
        else:
            rank.append(rank[num-1]+1)
        
    for num in range(len(alice)):
        if alice[num] > scores[0]:
            positions.append(1)
        elif alice[num] < scores[-1]:
            positions.append((rank[-1])+1)
        else: 
            position = binarysearch(alice[num], scores)
            positions.append(rank[position])
    return positions     
        
scores = [100,90,90,80,75,60]

alice = [50,65,77,90,102]

print(climbingLeaderboard(scores, alice))


73,73,73,71,71,71,71,71,71,70,70,69,69,68,68,68,68,67,
67,67,66,66,65,65,64,64,62,61,61,60,59,59,59,59,59,59,58,57,56,56,
55,55,53,52,52,51,51,51,51,51,51,51,51,51,51,51,51,51,50,50,50,50,
49,49,48,48,47,47,47,45,43,42,42,41,38,36,36,36,36,35,35,35,35,35,35,
34,34,34,33,33,33,33,33,32,30,28,28,28,28,27,27,27,26,23,23,22,22,20,
20,20,18,18,15,15,14,14,13,13,11,11,10,10,8,8,7,6,5,4,4,4,1,1,1,1,1,1,
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1