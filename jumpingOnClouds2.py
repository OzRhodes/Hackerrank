#jumpingOnClouds.py


def jumpingOnClouds(c):
    count = 0
    cloud = 0
    while cloud < len(c)-1:
        if cloud + 2 <= len(c)-1:
            count += 1
            if c[cloud + 2] == 0:
                cloud = cloud + 2
            else:
                cloud = cloud + 1
        else:
            count += 1
            cloud += 1
    return count 


c = [0,0,0,1,0,0]
print (jumpingOnClouds(c))