#flatlandSpaceStations.py


def flatlandSpaceStations(n, c):
    max_seg = 0
    max_dist = 0
    cities = []
    first_seg = True
    #create an array of cities and establish if it has a station attached
    for i in range(n):
        cities.append(-1)
    for i in range(len(c)):
       cities[c[i]]=1
       
    for i in range(len(cities)):
        if cities[i] == -1:
            max_seg +=1
            if i == len(cities)-1:
                max_dist = max(max_dist, max_seg)
                max_seg = 0
        elif first_seg:
            max_dist = max(max_dist, max_seg)
            max_seg = 0
            first_seg = False
        else:
            max_dist = max(max_dist, int((max_seg + 1)/2))
            max_seg = 0

    return max_dist
    



n = 5
c = [0,4]
print(flatlandSpaceStations(n, c))

'''
func flatlandSpaceStations(n: Int, c: [Int]) -> Int {
    var maxSegment = 0
    var maxDistance = 0
    var cities = Array(0..<n)
    for i in c {
        cities[i] = -1
    }
    
    var firstSegment = true
    for j in 0..<cities.count {
        if cities[j] != -1 {
            maxSegment += 1
            if j == cities.count - 1 {
                maxDistance = max(maxDistance, maxSegment)
                maxSegment = 0 
            }
        } else if firstSegment {
                maxDistance = max(maxDistance, maxSegment)
                maxSegment = 0 
                firstSegment = false
        } else {
            maxDistance = max(maxDistance, (maxSegment + 1) / 2)
            maxSegment = 0
        }
    }
    return maxDistance
}'''