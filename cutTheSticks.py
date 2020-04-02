#cutTheSticks.py

def cutTheSticks(arr):
            output=[]
    while sum(arr)>0:    
        output.append(len(arr))
        cut = min(arr)
        for stick in range (len(arr)):
            arr[stick] -= cut
        for stick in reversed(range(len(arr))):   
            if arr[stick] == 0:
                arr.remove(arr[stick])
                
    return output


arr=[1,2,3,4,3,3,2,1]
cutTheSticks(arr)